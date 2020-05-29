# ROexamTesting
In questo repo organizziamo il punto di incontro tra gli sviluppatori e gli studenti coinvolti nel beta-testing di quello che sarà il sistema per i temi dell'esame di Ricerca Operativa 2020.
Il repo contiene istruzioni a vario livello ed anche temi fac-simile per quello che sarà l'esame.

## Prime istruzioni

1. I Jupyther Notebooks non girano da remoto e, pertanto,
   come prima cosa da fare, devi ricopiarti il contenuto di questo repo in locale.
   Vi sono due principali alternative su come farlo,
   esplorate nell'appendice <a href="#ricopiaInLocale">Come Ricopiare questo repo in locale, e come mantenerne aggiornato nei contenuti</a>

2. Portati nella cartella `ROexamTesting/config/`
   e leggi il file `how_to_start.md` e seguine le indicazioni per predisporre l'ambiente.

3. dalla cartella `ROexamTesting`, una volta attivato l'ambiente,
   lancia `jupyter-notebook` ed utilizza Jupyther nel browser
   per visualizzare e testare i notebooks con gli esercizi.

4. Se rilevi un problema nell'utilizzo dei notebooks con gli esercizi,
   o dei malfunzionamenti nel sistema sviluppato per l'esame,
   utilizza i meccanismi di GitHub per facilitare la collaborazione:
   apri una issue nel repo per richiedere le nostre correzioni od integrazioni.

5. Se sei bloccato e lo reputi più efficace, scrivi direttamente nel gruppo Telegram dei beta-tester,
   cui puoi auto-iscriverti al link:
```
   https://t.me/joinchat/EDaVmBl39deQMumY7g8U8w
```
   Vi ringraziamo per ogni spunto, feedback, o richiesta di aiuto.

# Appendice: Come Ricopiare questo repo in locale, e come mantenerne aggiornato nei contenuti

<a name="ricopiaInLocale">Il modo più rapido e flessibile</a>
    per farlo è lanciare il seguente comando da terminale:
```
git clone https://github.com/romeorizzi/ROexamTesting.git
```
questo comando richiede però che tu abbia `git` installato sulla tua macchina.

Se non lo hai o non vuoi rapportarti col terminale nè contribuire con parti tue al repo ma solo fruirne come di un tutorial per predisporti all'esame,
allora, dal repo su GitHub nel tuo browser premi il bottone verde "Clone or Download" in alto a destra
   e scaricati lo `.zip` file in locale. Poi decomprimilo, non ti servirà altro per poter testare ed utilizzare ogni cosa, e potrai comunque farci avere il tuo feedback.

Quando ti dovesse interessare la possibilità di contribuire attivamente ad un qualche progetto in collaborazione
(ad esempio in questo sei ben venuto) allora sarà venuto per te il momento di venire a conoscere `git`. Potrai allora installartelo come dalle seguenti istruzioni.

[Istruzioni per installare `git` sulla tua macchina](https://www.html.it/pag/53180/installazione-di-git/)

Avere `git` installato sulla tua macchina potrà aiutarti anche perchè noi aggiungeremo esercizi e componenti da testare un pò alla volta, man mano che li abbiamo pronti. Inoltre andremo via via aggiornandoli e migliorando le istruzioni grazie anche alle vostre segnalazioni di malfunzionamenti e richieste di chiarimenti.
Quindi ti converrà aggiornare periodicamente quanto hai scaricato dal repo. Potrai sempre cancellare la cartella in locale dove lo hai ricopiato e riscaricarlo. Tuttavia il modo più semplice per farlo è di lanciare il seguente comando da dentro tale cartella (o da qualsiasi sua sottocartella):

```
git pull
```
