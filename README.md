# ROexamTesting

Questo repository è il punto di incontro tra gli sviluppatori e gli studenti coinvolti nel beta-testing di quello che sarà il sistema per i temi dell'esame di Ricerca Operativa dal 2020 in poi.

Il repo conterrà istruzioni a vario livello e anche dei fac-simili di temi esame.

## Documentazione: il sistema di pagine Wiki

Le pagine Wiki di questo repo GitHub contengono istruzioni che ti guideranno in tutte le fasi di installazione necessarie.
Anche se le istruzioni saranno spesso di tipo passo passo e potrai ricopiarne i codici, ti converrà comunque mantenerti vigile, critico e consapevole di cosa fanno.

Ti consigliamo in particolare di attenerti all'impiego meticoloso degli __environments__.
Pertanto, prima di installare pacchetti, crea un environment e attivalo, in modo da isolarti dentro di esso a garanzia sia sua
(per le installazioni per l'esame di Ricerca Operativa) sia di ciò che sta fuori (altre installazioni sulla tua macchina).

Per accedere alla [pagina Wiki principale](https://github.com/romeorizzi/ROexamTesting/wiki) di un repo su GitHub basta cliccare sul suo tag di scheda posizionato nella barra in alto, disposta orizzontalmente sotto il nome del repository.
Oppure puoi andare direttamente all'URL della pagina, che in questo caso è:

[`https://github.com/romeorizzi/ROexamTesting/wiki`](https://github.com/romeorizzi/ROexamTesting/wiki)
 

## Aiuto e segnalazione di problemi

Se rilevi un problema nell'utilizzo dei notebooks con gli esercizi, o dei malfunzionamenti nel sistema sviluppato per l'esame,
o semplicemente ti serve aiuto, puoi scrivere direttamente nel gruppo Telegram dei beta-tester, a cui puoi auto-iscriverti al link:
```
   https://t.me/joinchat/EDaVmBl39deQMumY7g8U8w
```

In alternativa, ti incoraggiamo a utilizzare anche per questo i meccanismi di GitHub per facilitare la collaborazione:
   puoi aprire un'issue nel repo per richiedere le nostre correzioni o integrazioni (vedi la scheda _Issues_ in cima a questa pagina di GitHub).

In ogni caso, _vi ringraziamo per ogni spunto, feedback, o richiesta di aiuto_.


## Come ricopiare questo repo in locale (e come mantenerlo aggiornato nei contenuti)

<a name="ricopiaInLocale">Il modo più rapido e flessibile</a>
    per farlo è lanciare il seguente comando da terminale:
```
git clone https://github.com/romeorizzi/ROexamTesting.git
```
questo comando richiede però che tu abbia `git` installato sulla tua macchina.

Se non lo hai o non vuoi rapportarti col terminale, né contribuire con parti tue al repo ma solo fruirne come di un tutorial per predisporti all'esame, allora, dal repo su GitHub nel tuo browser premi il bottone verde "Clone or Download" in alto a destra, scarica il file `.zip` in locale e poi decomprimilo. Non ti servirà altro per poter testare ed utilizzare ogni cosa, e potrai comunque farci avere il tuo feedback.

Quando ti dovesse interessare la possibilità di contribuire attivamente a un qualche progetto di collaborazione
(per esempio in questo sei benvenuto), allora verrà per te il momento di conoscere meglio `git`. Potrai allora installartelo seguendo la guida qui riportata: 

[Istruzioni per installare `git` sulla tua macchina](https://www.html.it/pag/53180/installazione-di-git/)

Avere `git` installato sulla tua macchina potrà aiutarti anche perchè noi aggiungeremo esercizi e componenti da testare un pò alla volta, man mano che li abbiamo pronti. Inoltre andremo via via aggiornandoli e migliorando le istruzioni grazie anche alle vostre segnalazioni di malfunzionamenti e richieste di chiarimenti.
Quindi ti converrà aggiornare periodicamente quanto hai scaricato dal repo, magari controllando la presenza di nuovi file prima di lavorarci, tramite il comando

```
git fetch
```

Il modo più semplice poi per scaricare in locale i file nuovi e/o quelli aggiornati è di lanciare il seguente comando da dentro tale cartella (o da qualsiasi sua sottocartella):

```
git pull
```

Se però tu o i tuoi programmi avrete modificato dei file in locale, il pull non andrà in porto per non rischiare di sovrascrivere tuoi file e ti verrà segnalato un conflitto. Se conosci `git` avrai molti modi per risolverlo.
Ma, se sei inesperto, non spaventarti né bloccarti:
ricorda che potrai sempre cancellare la cartella dove hai ricopiato il repo in locale, e riscaricarlo da capo da questo sito nella versione aggiornata.


