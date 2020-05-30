# *Ricerca Operativa 2020*<br> come predisporre l'ambiente per poter utilizzare, testare, o sviluppare i Notebooks dei temi o dei loro fac-simile

Gli ecosistemi che girano attorno a Python sono una macchina da corsa a motore aperto. Questo può essere eccitante e certo vi è tanta potenza di cui impadronirsi, tanto movimento ed interazione, e tante opportunità di innovazione, collaborazione, e crescita, ma anche tante occasioni per andare a sbattere la testa contro un muro se non si seguono alcune accortezze.
Il rischio tipico (la peste di Python) è quello di incedere troppo alla leggera quando si deve aggiungere componenti (elementi di libreria detti pacchetti) per poter far girare un software o sistema in cui siamo interessati.
E' un operazione facile per la quale si utilizza tipicamente uno dei seguenti strumeti all'uopo preposti:

- `conda` (vi suggeriamo questo)

- `pip` (più generale di conda, bene sapere che esiste, ma non vi è necessario)

- `python -m` (in realtà, col paramentro `-m`, python stesso può fare quanto fà pip, e si otterrebbe anche maggiore controllo)

Impareremo ad usare questi comandi (anzi, solo `conda`, tanto ci basta ai nostri scopi ed i concetti sottostanti che quì ci preme tu acquisisca sono gli stessi) per portare a casa il nostro obiettivo (far girare in modo sicuro gli esami di Ricerca Operativa senza creare incompatibilità o problemi di versioni in alcun dove della tua macchina; e sapere come si affrontano gli eventuali problemi ove dovessero essere già presenti). Per questo, oltre che dettagliarvi istruzioni passo passo, cercheremo anche di rendervi consapevoli di cosa state facendo e di dove sono i pericoli. Con questa conoscenza, usando la testa, non andrete a farvi male nemmeno con `pip` o `python -m` qualora doveste preferire questi strumenti più ampi per un uso più specifico o di fino.
Come ulteriore motivazione a proseguire in questa lettura: le cose spiegate quì sono valide anche al di fuori dell'esame di Ricerca Operativa. Sono pervasive a `python` (e in realtà non solo a questo linguaggio).

Ecco il punto:

Utilizzare `conda` (oppure `pip`, o quello che preferisci, alla fine la storia è la stessa) per installare un nuovo componente è facile e subito fatto, specie se sei disposto a farlo con qualche martellata (ad esempio con un `sudo pip install`) ma il problema è che se sei inesperto (ossia non lo hai ancora preso in quel posto oppure non hai ancora capito da dove è arrivato), probabilmente hai scelto la strada più breve in modo troppo inconsapevole e ti stai scavando la fossa compromettendo le cose nel futuro.
E puoi star certo che quel futuro arriverà fin troppo presto e puntuale.

Tutti quando andiamo al supermercato ci facciamo prendere dalla sindrome di riempire il carrello, ed in effetti ci sono così tante librerie belle da sperimentare. Ed è giusto farlo, giusto e possibile provare un pò di tutto, ma con testa.
Non possiamo buttare tutto insieme alla rinfusa dentro nello stesso carrello perchè si creano delle incompatibilità sicuro come l'olio. Alcuni componenti assumono certe dipendenze, in una ben precisa versione, e anche per il solo fatto che gli aggiorni la versione di quel componente mica è detto che funzionino meglio: no, smettono di funzionare e non sai più come uscirne a risolvere il problema.
Anzi, se a quel punto perdi la testa e cominci a muoverti senza sapere cosa stai facendo (senza aver capito e fatto tuo quanto stiamo cercando di dirti quì) rischi di introdurre conflitti in circolo così che alla fine nessun software potrà più funzionare, nè i più vecchi nè l'ultimo installato.
Pertanto, quando ti installi qualcosa, e potrebbe anche essere il software migliore e più curato e sicuro e stabile di questo mondo, potresti pertanto compromettere la precedente installazione di altri software presenti sulla tua macchina. L'introduzione di una cosa nuova manda fuori briscola cose venute prima (se poi fai sudo agisci a livello di sistema invece che di utente e potresti compromettere la stessa installazione di sistema di python).

Vi vogliamo tutti in grado di partecipare al beta-testing coi temi fac-simile e poi all'esame. Anzi, ci piacerebbe promuovere il brake on through to the other side (https://www.youtube.com/watch?v=-r679Hhs9Zs), dove ci aiutate a migliorare il sistema, i materiali, la documentazione.
Per non incorrere in problemi di versioni disallineate tra di noi,
e per non compromettere le installazioni sulla tua macchina,
ti insegnamo innanzitutto come fare a gestire quelli che sono chiamati gli environments.
Ecco il concetto ed il consiglio:

| <img src="../images/alert.jpeg" alt="Avviso!" style="width:40px;"/> | Vedi di organizzarti ed essere sistematico nell'uso degli _environments_. |
| :------------- | -----------: |

L'idea è che ogni volta che vai a fare la spesa ti porti un carrellino nuovo (environment), che usi per metterci dentro tutto quello che serve per quel particolare scopo (ad esempio l'esame di Ricerca Operativa) evitando di compromettere altri sistemi che hai già sulla tua macchina, od altri environment che hai configurato con cura (e magari utilizzi per collaborare ad un progetto su una piattaforma che deve essere comune). Al tempo stesso ti assicurerai in questo modo che anche installazioni future non possano inficiare il tuo environment per l'esame di Ricerca Operativa od altri tuoi progetti.
Un ultima cosa: usare la testa significa innanzitutto non farsi prendere da sentimenti negativi come lo scoramento od il panico. Sappi al contrario che:

- con questo semplice accorgimento ed attenzione ad usare scrupolosamente gli environments potrai provare tutti i prodotti del supermercato (e per molti ne vale la pena, può esserti anzi necesario) senza correre alcun pericolo. Potrai inoltre collaborare su una base comune con persone che operino da qualunque piattaforma o sistema operativo senza doverti preoccupare troppo di questi aspetti che a rigore dovrebbero essere secondari.

- se ti ritrovi con una situazione compromessa, potrai sempre ripartire da capo.

- per l'esame di Ricerca Operativa ti facciamo noi la lista della spesa (si trova nel file `requirements.txt`) e, a dire il vero, una tale lista della spesa è resa disponibile dalla maggior parte delle librerie serie che hanno delle dipendenze (quindi come usare il file `requirements.txt` è un altra competenza che ti porterai via con la presente lettura).

Abbastanza teoria, passiamo ai fatti.

Ok, facciamo l'ipotesi di usare `conda` (se usi altri sistemi la teoria è la stessa, ossia vedi di fare le cose analoghe a quelle descritte quì).


Lanciando da terminale il comando:

```
conda env list
```

scopri la lista dei tuoi environment attuali. Se sei utente a rischio probabilmente ne trovi uno solo. Allora questa guida fà proprio per tè, è stata scritta per la tua salvezza.

Per creare il tuo environment per l'esame di Ricerca Operativa:

```
conda create --name ROexam --file requirements.txt
```

Se vuoi controllare che abbia funzionato lista di nuovo i tuoi environment attuali e vedi se è stato aggiunto.

Se è stato aggiunto sei a cavallo, ricordati solo di attivarlo prima di utilizzarlo.
Ah, da terminale l'attivazione si fà con:

```
conda activate ROexam
```

Vedi come cambia il prompt? Serve perchè tu abbia sempre presente da che environment tu lanci i tuoi comandi ed applicazioni. Facci quindi attenzione.

L'attivazione e selezione di un particolare environment può anche essere fatta da dentro `Jupyther`, in particolare se utilizzi `JupytherLab` (interfaccia più evoluta per i Jupyther Notebooks che ti consigliamo di utilizzare non appena avrai acquisito una comprensione base di cosa siano i Jupyther Notebooks) e, in modo ancora più agevole, da dentro `Anaconda`.
Di fatto ti consigliamo di utilizzare o il terminale o `Anaconda`, da `Jupyther` le cose non sono sempre quelle che sembrano.

E se invece nel crare l'environment hai ottenuto dei problemi?

Proviamo a listare quì i problemi plausibili, più tutti quelli ad oggi segnalatici da tuoi compagni (__se hai problemi ulteriori contattaci presentandoci in chiarezza gli estremi del nuovo problema in cui ti sei imbattuto__, dopo averti prestato soccorso lo aggiungeremo a questa lista quì sotto insieme alle istruzioni su come affrontarlo):

1. alcuni dei componenti richiesti, come specificati nel file `requiremnts.txt` da noi fornito, non sono reperibili sui canali attualmente previsti nella tua installazione locale.
Questo problema si manifesta con qualcosa del tipo:
```
(base) romeo@romeo-HP-ProBook-450-G4:~/corsi/RO/jupyther/ROexamTesting/config$ conda create --name ROexam --file requirements.txt
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - ipysheet==0.4.3

Current channels:

  - https://repo.anaconda.com/pkgs/main/linux-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/r/linux-64
  - https://repo.anaconda.com/pkgs/r/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.

```
Mh..., come fare?
Io ho googlato "PackagesNotFoundError: ipysheet==0.4.3"
ed ho optato per il secondo hit (dal primo hit "Spreadsheet widget for the Jupyter Notebook — ipysheet 0.4" da ipysheet.readthedocs.io capisco a cosa serve quel componente, ma probabilmente non trovo il channel dove reperirlo, non sembra specifico a quello, semmai lo guardo dopo).
Al secondo hit ("PackagesNotFoundError: The following packages are not ...") da stackoverflow.com mi attendo di ricevere aiuto al mio stesso problema.

Tra i suggerimenti a quella richiesta di aiuto su stackoverflow trovo:

Try adding the conda-forge channel to your list of channels with this command:
```
conda config --append channels conda-forge
```

Poi rilancio il comando di creazione dell'environment:

```
conda create --name ROexam --file requirements.txt
```
Eccoci cioè di nuovo alla cassa col nostro bel carrellino della spesa (nel file `requirements.txt`) e questa volta mi dice che per lui va bene e mi precisa una lunga lista di pacchetti che verrà installata se gli dò il mio consenso a proseguire:

```
...
Proceed ([y]/n)?
```

gli dico di sì felice come una pasqua, sicuro che tanto tutta questa roba finirà dentro un environment separato di nome `esameRO` e che sarà contenuta lì dentro come dentro in una bolla, non potrà mettere fuori fase altre bolle (sorry, environments; scusate, carrelli della spesa) e che potrò sempre chiedere la cancellazione di questa bolla (con disinstallazione automatica di tutto quanto contiene, dato che è contenuto entro essa) e con la possibilità di rifarla da zero se per caso l'avevo sporcata con qualche installazione sbagliata (perchè magari mi ero dimenticato di attivare e portarmi nel giusto environment prima di aggiungere packages, oppure semplicemente perchè avevo voluto sperimentare l'aggiunta di un nuovo componente per rendere più intriganti i temi di Ricerca Operativa e contribuire in qualche modo al progetto (brake on through, brake on through, yeah)).

Ed ecco come attivare l'environment per poterlo usare od anche ampliare ulteriormente (installarci ulteriori pacchetti per sperimentare):

```
conda activate env_2
```
Hai capito giusto: possiamo anche aggiungere altri pacchetti dentro questo environment, ossia espandere questa bolla.
Se la nuova bolla ci piace possiamo anche decidere di trasformarla nella lista della spesa di cosa serva per costruirne una uguale per poterla riprisitinare rapidamente in futuro o condividerla con altri o magari anche suggerire di renderla parte del progetto con una pull request al repo git.

```
conda list -e > requirements.txt
```

oppure

```
pip freeze > requirements.txt
```


Alcune pagine con spiegazioni correlate:

- [perchè non fare sudo pip install ed ulteriori approfondimenti che però non ti dovrebbero nemmeno servire se hai il terminale](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/)

- [Jupyter Notebook for Beginners: A Tutorial (che entra in questioni anche tecniche)](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)

- [Why and How to make a Requirements.txt](https://medium.com/@boscacci/why-and-how-to-make-a-requirements-txt-f329c685181e)

- [To package a conda environment (Requirement.txt and virtual environment)](https://gist.github.com/pratos/e167d4b002f5d888d0726a5b5ddcca57)
