# ROexamTesting
In questo repo organizziamo il punto di incontro tra gli sviluppatori e gli studenti coinvolti nel beta-testing di quello che sarà il sistema per i temi dell'esame di Ricerca Operativa 2020.
Il repo contiene istruzioni a vario livello ed anche temi fac-simile per quello che sarà l'esame.

## Prime istruzioni e Workflow entro il quale operare

1. Ti consigliamo di installarti innanzitutto [Anaconda Individual Edition](https://jupyterlab.readthedocs.io/en/stable/), una componente invero non necessaria ma che ti potrà rendere le cose più facili, specie se sei inesperto nel gestire le installazioni e gli ambienti, e ti consentirà agevolmente un ventaglio di possibilità ulteriori.
Un ambiente che ti renderà particolarmente agevole gestire gli environment e sperimentare una grande varietà di applicazioni che potrebbero esserti interessanti anche in altre occasioni è l'[Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/).
L'uso di questo strumento potrebbe rivelarsi il compagno ideale per chi non vuole gestire le cose da terminale.  

2. Il tuo esame avverrà dentro un [Jupyther Notebook](https://jupyter.readthedocs.io/en/latest/) con cui interagirai sulla tua macchina, dentro il browser.
   Buona notizia: se ti sei installato Anaconda hai già, e già correttamente installato,
   il software che serve per far girare i Jupyther Notebook
   sulla tua macchina e dentro il tuo browser.
   In caso contario, ti consigliamo di tornare al punto 1 della presente lista, anche se sei già nella situazione che i Jupyther Notebook girano correttamente sulla tua macchina.
   Se non vuoi installarti Anaconda perchè non hai spazio per installarti tutto quel ben di dio, considera la possibilità di installarti `conda`, la sua versione mignon pensata proprio per chi avesse questi problemi.

   ok, come prerequisito non ti basta avere che i Jupyther Notebook girino correttamente sulla tua macchina ma è anche utile che tu abbia almeno una vaga idea di cosa puoi farci (anche al di là di questo esame) e acquisisca una conoscenza base di come muoversi entro essi.
  Al link [Jupyther Notebook](https://jupyter.readthedocs.io/en/latest/) dato sopra non solo trovi come eseguire l'installazione ma anche dei tutorial che ti converrà esplorare (solo in piccolissima parte, limitati alla punta dell'iceberg) almeno per un primo acclimatamento nell'ambiente e comprenderne le potenzialità che potrebbero servirti prima come studente e poi nella tua carriera.
   Se conosci già l'ambiente dei Jupyther Notebook col quale comunque ti consigliamo di muovere i tuoi primi passi, e appena ti senti abbastanza sicuro e spavaldo, forse porebbe interessarti utilizzare invece  
   [JupytherLab](https://jupyterlab.readthedocs.io/en/stable/) che offre diversi vantaggi ed anche è incluso nella distribuzione di Anaconda.

3. I Jupyther Notebooks non girano da remoto ma in locale. Devi pertanto ricopiarti in locale il contenuto di questo repo, ossia i materiali specifici all'esame (esercizi ed infrastruttura).
   Vi sono due principali alternative su come farlo,
   esplorate nell'appendice <a href="#ricopiaInLocale">Come Ricopiare questo repo in locale</a> in calce a questo documento (siamo nel file `README.md` del repo in questione).

4. Attenzione: non basta scaricarsi in locale i contenuti specifici all'esame, devi anche installare le librerie di infrastruttura e settare un ambiente dove mandare in esecuzione il tutto.
   Una cosa buona è che in realtà queste due fasi (punti 3 e 4) sono in tutto indipendenti, puoi eseguirle nell'ordine che preferisci o condurle in modo indipendente o in parallelo, avanzando con una intanto che ti rispondiamo a una richiesta di aiuto sull'altra.

   Come procedere su 4?
   Portati nella cartella `ROexamTesting/config/`
   e leggi il file `how_to_start.md` e seguine le indicazioni per predisporre l'ambiente.
   Due buone notizie:

  -  compresi i semplici concetti di base (che potranno servirti anche altrove) serve poi solo un pizzico di auto-disciplina a metterli in pratica per evitare ogni possibile difficoltà nelle installazioni;

  -  l'ambiente non dovrebbe richiedere tanti aggiornamenti quanti i contenuti (e tra 3 e 4 vale l'indipendenza di cui sopra).

  Resta però importante tu comprenda cosa siano gli _environment_ e te ne crei uno specifico per l'esame di Ricerca Operativa. In realtà ti converrà avvalerti di questo stesso strumento anche in altri contesti per evitare conflitti tra le librerie che installi sulla tua macchina.

5. dalla cartella `ROexamTesting`, una volta attivato l'ambiente che hai creato appositamente,
   lancia `jupyter-notebook` ed utilizza Jupyther nel browser
   per visualizzare e testare i notebooks con gli esercizi.

6. Se rilevi un problema nell'utilizzo dei notebooks con gli esercizi,
   o dei malfunzionamenti nel sistema sviluppato per l'esame,
   o semplicemente ti serve aiuto,
   scrivi direttamente nel gruppo Telegram dei beta-tester,
      cui puoi auto-iscriverti al link:
   ```
      https://t.me/joinchat/EDaVmBl39deQMumY7g8U8w
   ```
      In alternativa, ti incoraggiamo ad utilizzare anche per questo i meccanismi di GitHub per facilitare la collaborazione:
      apri una issue nel repo per richiedere le nostre correzioni od integrazioni (vedi la tag "Issues" in cima a questa pagina di GitHub).

      In ogni caso, _vi ringraziamo per ogni spunto, feedback, o richiesta di aiuto_.

## Appendice: Come Ricopiare questo repo in locale (e come mantenerlo aggiornato nei contenuti)

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
