## Modellizzazione ##

La GiuseppeRospo S.p.A. è specializzata nella produzione di pasta. In particolare, i prodotti più venduti sono cinque: le penne rigate, le conchiglie, gli spaghetti, i tortiglioni e i ravioli. I prodotti sono realizzati seguendo un processo di lavorazione, che include una fase di trafilatura per dare alla pasta la forma desiderata. La GiuseppeRospo S.p.A. possiede due macchinari per la trafilatura, M1 e M2, che in base al tipo di prodotto impiegano tempi diversi.
La macchina M2 è la versione aggiornata della macchina M1, perciò è in grado di compiere la stessa operazione un po’ più velocemente.
Nella tabella seguente sono indicati i minuti richiesti per la trafilatura di ogni prodotto se processato con la macchina M1 oppure con la macchina M2.

| PRODOTTO     | TEMPO SU M1 | TEMPO SU M2 |
|--------------|-------------|-------------|
| Penne rigate | 14          | 10          |
| Conchiglie   | 18          | 14          |
| Spaghetti    | 10          | 8           |
| Tortiglioni  | 15          | 11          |
| Ravioli      | 10          | 7           |


__Richieste__:
1. Formulare il problema come problema di Programmazione Lineare Intera, motivando le scelte compiute in una cella Markdown o Raw (3 punti)
2. Risolvere il problema sfruttando la libreria Pulp, trovando come assegnare i cinque prodotti alle due macchine in modo da minimizzare il _makespan_ (i.e., la durata complessiva della lavorazione, dall’inizio alla fine) (5 punti)
3. E se invece si volesse minimizzare l’attesa totale dei prodotti per essere lavorati, come cambierebbe la funzione obiettivo? E il suo valore all'ottimo? (2 punti)
