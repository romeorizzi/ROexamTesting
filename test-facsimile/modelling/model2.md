## Modellizzazione ##

Grafito, il nuovo direttore di un museo di quadri di alto valore, decide di installare un sistema di telecamere di sorveglianza a circuito chiuso e si pone quindi il problema di determinare il numero minimo di apparecchi necessari. La pianta del museo è rappresentata nella figura sottostante:

![](modelling/model2-map.png?raw=true)

Le telecamere richiedono una diffusione della luce incompatibile con le esigenze di conservazione del materiale esposto pertanto il direttore decide di installarle negli incroci tra i corridoi.

__Richieste__:
1. Formulare un modello di Programmazione Lineare Intera che aiuti Grafito a minimizzare il numero di telecamere installate, sapendo che ogni corridoio deve essere coperto da almeno una telecamera, motivando le scelte compiute in una cella Markdown/Raw (3 punti)
2. Risolvere il problema sfruttando la libreria Pulp (5 punti)
3. Le telecamere tuttavia non hanno tutte lo stesso prezzo. Nella tabella seguente sono indicati i singoli costi di attivazione per ognuna di esse.

| TELECAMERA | COSTO |
|:----------:|:-----:|
|      a     |   5   |
|      b     |   10  |
|      c     |   20  |
|      d     |   6   |
|      e     |   4   |
|      f     |   5   |

Quali telecamere bisognerebbe attivare per garantire la copertura e minimizzare i costi totali?
