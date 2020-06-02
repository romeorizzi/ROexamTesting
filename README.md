# ROexamTesting

Questa repository è il punto di incontro tra gli sviluppatori e gli studenti coinvolti nel beta-testing di quello che sarà il sistema per i temi dell'esame di Ricerca Operativa dal 2020 in poi.

La repo conterrà istruzioni a vario livello sulle installazioni e configurazioni da apportare sulla tua macchina per predisporla all'esame, e si propone di crescere parallelamente ad ogni difficoltà da voi riscontrata e fatta presente
durante la fase di testing e verifica.
Il repò continuerà pertanto a crescere in modo dinamico, sia per mano vostra (contribuirete con le vostre domande e segnalazioni) che nostra.

Per mano nostra la repo andrà arricchendosi via via di esercizi fac-simile per quello che sarà il tuo tema d'esame.
Le tipologie delle competenze richieste ed invero degli stessi esercizi
sono in realtà quasi in tutto le stesse di quelle dei temi delle edizioni precedenti.
L'[archivio di tali temi con correzzioni annesse](http://profs.sci.univr.it/~rrizzi/classes/RO/info_esami/)
resta pertanto, anche per estensione oltre che per stabilità,
il riferimento più valido per farsi un'idea dell'ampio spettro delle domande
che potremmo fare e delle tue competenze che potrebbero trovare valorizzazione in punti-voto al momento dell'esame (il nostro approccio non è di guardare a quello che uno non sà ma a quello che uno sà, o meglio sulle competenze che ha ed è in grado di esprimere).
Resta che il taglio di come poste le domande potrà via via shiftare rispetto a quanto era sul cartaceo, magari anche nel tempo mano a mano che prendiamo consapevolezza insieme di cosa consentito coi nuovi supporti.
Gli esercizi che trovi in questo repo rivelano questi shift in anteprima.
La differenza principale con quanto prima del 2020 stà infatti nel fatto che l'esame quest'anno non avverrà su carta ma sul tuo PC da casa.
Avverrà dentro un foglio Jupyter (`Jupyter Notebook`), e questo porta inevitabilmente a ruotare alcune consegne e ci consente di precisarle in modo più puntuale, come sempre avremmo voluto fare (ed alto è stato il nostro sforzo in questo negli anni, tanto da predisporre per questa evoluzione). Puntiamo ad introdurre gradualmente dei supporti che possano rendere più piacevole ed autentica l'esperienza dell'esame:
nella nostra visione il Jupyter Notebook potrà fornirti parziali validazioni dei tuoi certificati di SI o di NO. Lo stesso feedback e la qualità dell'interazione consentita dentro il Jupyter Notebook potrà andare migliorando gradualmente
man mano che avanzeremo nella realizzazione dei supporti (è un progetto in cui sei invitato ad entrare anche come modalità alternativa di sostenere l'esame).
Se tu dovessi ritrovarti con un applet che non funziona, oltre che a segnalarcelo (non all'esame dove ormai serve poco ed alzerebbe solo la confusione), niente paura:
eventualmente rinunciando ad utilizzare l'applet più figo e/o a dei feedback
di supporto ti sarà comunque sempre consentito di fornire le tue risposte in modalità testuale pura (accertandoti però di aderire allo spirito della consegna utilizzando il tuo senso critico piuttosto che un verificatore od un editor guidato od applet di supporto). Quindi, non appena avrai installata una versione funzionante di Jupyter sarai già in condizione di condurre il tuo esame dimostrando la tua competenza. Per avere l'intero video-gioco con tutte le features e supporti segui con cura le istruzioni ed eventualmente chiedine altre.



## Documentazione: il sistema di pagine Wiki

Le pagine Wiki di questa repo GitHub contengono istruzioni che ti guideranno in tutte le fasi di installazione necessarie.
Anche se le istruzioni saranno spesso di tipo passo passo e per tua praticità potrai ricopiare i comandi nel tuo terminale (ricorda: nel mondo grafico usi `Ctrl-C` per ricopiare nella clipboard e `Ctrl-V` per richiamare dalla clipboard. Nel terminale usi invece `Ctrl-Shift-C` e `Ctrl-Shift-V` ma la clipboard è la stessa e quindi puoi portare le cose da un mondo all'altro), ti converrà comunque mantenerti vigile, critico e consapevole di cosa fanno i comandi ricopiati per essere pronoto a trovare soluzioni in caso di difficoltà (anche se risolvi autonomamente considera se opportuno farci sapere per offrire aiuto ai compagni).

Ti consigliamo in particolare di attenerti all'impiego meticoloso degli __environments__.
Pertanto, prima di installare pacchetti, crea un environment e attivalo, in modo da isolarti dentro di esso a garanzia sia sua
(per le installazioni per l'esame di Ricerca Operativa) sia di ciò che sta fuori (altre installazioni sulla tua macchina).

Per accedere alle [pagine Wiki](https://github.com/romeorizzi/ROexamTesting/wiki) di un repo su GitHub basta cliccare sul tag della scheda _Wiki_ posizionato nella barra disposta in cima alla pagina del repository.
Oppure puoi andare direttamente all'URL della pagina, che in questo caso è:

[`https://github.com/romeorizzi/ROexamTesting/wiki`](https://github.com/romeorizzi/ROexamTesting/wiki)
 

## Aiuto e segnalazione di problemi

Se rilevi un problema nell'utilizzo dei notebooks con gli esercizi, o dei malfunzionamenti nel sistema sviluppato per l'esame,
o semplicemente ti serve aiuto, puoi scrivere direttamente nel gruppo Telegram dei beta-tester, a cui puoi auto-iscriverti al link:
```
   https://t.me/joinchat/EDaVmBl39deQMumY7g8U8w
```

In alternativa, ti incoraggiamo a utilizzare anche per questo i meccanismi di GitHub per facilitare la collaborazione:
   puoi aprire un'issue nel repo per richiedere le nostre correzioni o integrazioni (vedi la scheda _Issues_, sempre in cima a questa pagina di GitHub).

In ogni caso, _vi ringraziamo per ogni spunto, feedback, o richiesta di aiuto_.


## Come ricopiare questa repo in locale (e come mantenerlo aggiornato nei contenuti)

<a name="ricopiaInLocale">Il modo più rapido e flessibile</a>
    per farlo è lanciare il seguente comando da terminale:
```
git clone https://github.com/romeorizzi/ROexamTesting.git
```
questo comando richiede però che tu abbia `git` installato sulla tua macchina.

Se non lo hai il consiglio è non solo di installartelo:


[Istruzioni per installare `git` sulla tua macchina](https://www.html.it/pag/53180/installazione-di-git/)

ma anche di cominciare ad avvalertene da subito e magari anche di venire a conoscerlo ed integrarlo nei tuoi workflow anche come forma di investimento dalle ampie ricadute). 

Già avere `git` installato sulla tua macchina potrà facilitarti nelle installazioni che affronteremo insieme. Ma se vorrai cominciare ad avvalerti di questo potente e flessibile strumento gratuito per il versioning dei tuoi file, o per il loro backup in locale o nel cloud, o per poter collaborare a progetti, potrai allora venire a conoscere di più su questo strumento avvalendoti dei molti materiali che trovi in internet.

> **Per saperne di più:** Git è uno strumento potentissimo e praticissimo per promuovere la collaborazione su progetti condivisi, tanto che è stato alla basa dell'attuale fiorire dell'open source. Fu ideato da Torvald per consentire un più distribuito sviluppo di Linux, e ha poi avviato una profonda rivoluzione nel mondo del software. Più recentemente si stà affermando anche per consentire la condivisione in progetti che nulla hanno a vedere col codice, la programmazione, o l'informatica. Per questo si sono andate recentemente affermando interfacce grafiche che consentono l'uso di git senza passare per il terminale, come ad esempio `gitcraken`. (Noi comunque non sottaciamo i vantaggi che vengono con l'uso del terminale anche in questo contesto. Inoltre, se ti installi `git` su Windows nessuno mette in dubbio ti convenga scegliere l'installazione che ti offre di avere anche un terminale nello stesso bundle.) <br>A nostro avviso `git` và considerato ormai come una "enabling technology". E' grosso ma puoi venire a conoscere le sue funzionalità e servizi un pò per volta, man mano che ti servono. In rete trovi ottimi tutorial per cominciare. Procedi un passo alla volta, mano a mano che vedi che ti serve di più potrai ricercare in rete all'occorrenza e dischiudere un nuovo potere e servizio di questo tuo amico.

Avere `git` installato sulla tua macchina potrà aiutarti anche perchè noi aggiungeremo esercizi e componenti da testare un pò alla volta, man mano che li abbiamo pronti. Inoltre andremo via via aggiornandoli e migliorando le istruzioni grazie anche alle vostre segnalazioni di malfunzionamenti e richieste di chiarimenti.
Quindi ti converrà aggiornare periodicamente quanto hai scaricato dal repo.
Se vuoi solo controllare la presenza di nuovi aggiornamenti puoi farlo lanciando, da dentro la cartella `ROexamTesting`, il comando

```
git fetch
```

Il modo più semplice per scaricarti in locale gli eventuali file nuovi (tipicamente nuovi esercizi) e/o quelli aggiornati è di lanciare il seguente comando (sempre da dentro la cartella `ROexamTesting` o da qualsiasi sua sottocartella):

```
git pull
```

Se però tu o i tuoi programmi avrete modificato dei file in locale, il pull non andrà in porto per non rischiare di sovrascrivere tuoi file e ti verrà segnalato un conflitto. Se conosci `git` od approfondisci un pò riguardo ad esso, avrai molti modi per risolverlo.
Ma, se sei inesperto, non spaventarti né bloccarti:
ricorda che potrai sempre cancellare la cartella dove hai ricopiato la repo in locale, e riscaricarlo da capo da questo sito nella sua ultima versione.


Se opti (sconsigliato) per non avvalerti di git, puoi comunque fruire
di quanto offerto in questa repo come di un tutorial per predisporti all'esame.
Se però vorrai cimentarti con l'esercizio come all'esame dovrai quantomeno scaricarti i materiali in locale poichè i Jupyther Notebooks non possono essere eseguiti da GitHub.
Per fare il download, da questo repo su GitHub, da dentro il tuo browser, premi il bottone verde "Clone or Download" in alto a destra, scarica il file `.zip` in locale e poi decomprimilo. (_Nota:_ Quando la repo è ottenuta scaricando lo zip da GitHub e decomprimendolo, ne andrà poi subito cambiato il nome da `ROexamTesting-master` a `ROexamTesting`.)
Se non ti pesa dover ripetere queste operazioni ad ogni aggiornamento, allora avere `git` non ti sarà necessario per poter testare ed utilizzare ogni cosa, e potrai comunque farci avere il tuo feedback e richieste di aiuto
sia attraverso il canale Telegram che attraverso la pagina GitHub del repo.
Però ogni operazione ti sarà più faticosa, francamente non te lo consigliamo se non per visionare in modo rapido e solo parziale i materiali senza davvero procedere alle installazioni.


