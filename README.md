# ROexamTesting

In questo repo organizziamo il punto di incontro tra gli sviluppatori e gli studenti coinvolti nel beta-testing di quello che sarà il sistema per i temi dell'esame di Ricerca Operativa 2020.
Il repo contiene istruzioni a vario livello ed anche temi fac-simile per quello che sarà l'esame.

## Documentazione: il sistema di pagine Wiki

Nelle pagine Wiki di questo repo GitHub trovi istruzioni
che ti guidano in tutte le fasi delle installazioni di cui sopra.
Anche se le istruzione saranno spesso di tipo passo passo e potrai ricopiarne i codici, ti converrà comunque mantenerti vigile, critico e consapevole
di cosa fanno le varie istruzioni. Consigliamo in particolare di attenersi all'impiego meticoloso degli environments.
Pertanto, prima di installare pacchetti, si crei un environment
e lo si attivi, in modo da isolarsi dentro di esso a garanzia sua
(installazioni per l'esame di Ricerca Operativa)
e di ciò che stà fuori (altre installazioni sulla tua macchina).

Per accedere alla [pagina Wiki principale](https://github.com/romeorizzi/ROexamTesting/wiki) di un repo su GitHub basta pigiare sul suo tag di scheda posizionato nella barra coi tag delle schede.
Tale barra è posizionata in alto, disposta orizzontalmente.
Oppure puoi andare direttamente allo URL di quella pagina che in questo caso è:

[`https://github.com/romeorizzi/ROexamTesting/wiki`](https://github.com/romeorizzi/ROexamTesting/wiki)
 

## Aiuto e segnalazione di problemi

Se rilevi un problema nell'utilizzo dei notebooks con gli esercizi,
o dei malfunzionamenti nel sistema sviluppato per l'esame,
o semplicemente ti serve aiuto,
scrivi direttamente nel gruppo Telegram dei beta-tester,
   a cui puoi auto-iscriverti al link:
```
   https://t.me/joinchat/EDaVmBl39deQMumY7g8U8w
```

In alternativa, ti incoraggiamo a utilizzare anche per questo i meccanismi di GitHub per facilitare la collaborazione:
   apri una issue nel repo per richiedere le nostre correzioni od integrazioni (vedi la tag "Issues" in cima a questa pagina di GitHub).

In ogni caso, _vi ringraziamo per ogni spunto, feedback, o richiesta di aiuto_.


## Come ricopiare questo repo in locale (e come mantenerlo aggiornato nei contenuti)

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
Quindi ti converrà aggiornare periodicamente quanto hai scaricato dal repo.
Il modo più semplice per farlo è di lanciare il seguente comando da dentro tale cartella (o da qualsiasi sua sottocartella):

```
git pull
```

Se però tu od i programmi avranno modificato dei file in locale, il pull non andrà in porto per non rischiare di sovrascrivere tuoi file e ti verrà segnalato un conflitto. Se conosci `git` avrai molti modi per risolverlo.
Ma, se sei inesperto, non spaventarti nè bloccarti:
ricorda che potrai sempre cancellare la cartella dove hai ricopiato il repo in locale, e riscaricarlo da capo nella versione aggiornata.


