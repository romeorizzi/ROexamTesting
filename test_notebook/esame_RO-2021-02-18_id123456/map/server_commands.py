# -*- coding: utf-8 -*-
"""
@authors: Adriano Tumminelli, Rosario Di Matteo, Marco Emporio
"""


####################################
# SETTINGS
####################################
subdir = "modo_verif" # sotto-cartella dove prende i punti dei verificatori
gruppo_telegram = "https://t.me/RicercaOperativa2020"
date = "2021-02-22" #data dell'esame


import hashlib
import zipfile
import os
import os.path
import re
import json


def sha1_file(filename):
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

    sha1 = hashlib.sha1()

    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)

    return sha1.hexdigest()


def read_points(filename):
    if os.path.exists(filename):
        with open(filename) as json_file:
            return json.load(json_file)
    return None

map_save_path = map_save_path = "../consegna_esameRO-" + date + "/map_export.txt"


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def handler_get_all_points(params):
    total_points = []

    directories = [d for d in sorted(os.listdir(os.getcwd())) if os.path.isdir(d)]

    for dir in directories:
        if dir.startswith("esercizio_"):
            total_points.append(read_points(dir + "/"+subdir+"/points.txt"))

    return json.dumps(total_points)

def handler_save_map(params):

    if not "data" in params:
        return "error"

    data = params["data"][0]

    # generare nome della cartella dove collocare la consegna
    if os.path.exists('../consegna_esameRO-' + date):
        return "directory_error la cartella consegna_esameRO-" + date + " esiste già. Se vuoi procedere con nuova consegna rimuovila o spostala altrove."
    os.mkdir("../consegna_esameRO-" + date)
    fname_base = os.path.basename(os.getcwd()) + ".zip"
    fname = "../consegna_esameRO-" + date + "/" + fname_base
    print(fname)
    zipf = zipfile.ZipFile(fname, 'w', zipfile.ZIP_DEFLATED)
    zipdir('.', zipf)
    zipf.close()
    #salvataggio del file export_map.txt
    with open(map_save_path, "w") as f:
        f.write(data)
    sha1_str = sha1_file(fname)
    #salvataggio della firma
    with open("../consegna_esameRO-" + date + "/firma_anticipata.txt", "w") as f:
        f.write(
"""
Invia la seguente firma digitale del file '{filename}'

{sha1}

al Gruppo Telegram del Corso:
    {gruppo_telegram}

se non ti è pratico allora puoi mandare una mail a ENTRAMBI i seguenti indirizzi:
    romeo.rizzi@univr.it
    alice.raffaele@univr.it

Se non hai o perdi la connessione internet puoi inviare la firma digitale tramite SMS al seguente numero:
cel:+39.3518684000


ATTENZIONE: Non apportare modifiche allo zip altrimenti la firma digitale del file non corrisponderà piu' a quella calcolata.
(E non potremo accettarlo se non ci perviene esso stesso entro i tempi concordati per la consegna nonostante le sue grosse dimensioni.)
""".format(
        gruppo_telegram = gruppo_telegram,
        filename = fname_base,
        sha1 = sha1_str
    )
        )

    return "done Archivio dell'esame generato correttamente (lo trovi nella cartella 'consegna_esameRO-YYYY-MM-DD', sorella della cartella in cui hai svolto il tuo esame. Se vuoi riprodurre una nuova consegna devi prima rimuovere o spostare questa cartella.)\n\nProcedi subito alla tua sottomissione e chiusura dell'esame (istruzion nel file 'firma_anticipata.txt' che trovi nella cartella)"

handlers = {
    "save" : handler_save_map,
    "get_scores": handler_get_all_points
}

def handle_message(params):
    cmd_type = params['type'][0]
    if cmd_type in handlers:
        return handlers[cmd_type](params)
    return "error"
