## Programmazione Dinamica ##

Un robot R, inizialmente situato nella cella A1, deve portarsi nella sua home H situata nella cella G9.

|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| A | R |   |   |   |   |   |   |   | X |
| B |   |   | X |   | X | X |   |   |   |
| C |   | X |   |   |   |   |   |   |   |
| D |   |   | X |   |   | X |   |   |   |
| E |   |   |   | X |   |   |   |   |   |
| F |   |   | X |   | X |   |   |   |   |
| G |   |   |   | X |   |   |   |   | H |

I movimenti base possibili sono il passo verso destra (ad esempio dalla cella A4 alla cella A5) ed il passo verso in basso (ad esempio dalla cella A4 alla cella B4). Tuttavia il robot non puà visitare le celle occupate da un Pacman (indicate con la X). Quanti sono i percorsi possibili?

__Richieste__:
1. Quanti sono i percorsi possibili se la partenza e in A1? (1 punto)
2. E se la partenza è in C3? (1 punto)
3. E se con partenza in A1 il robot deve giungere in F6? (1 punto)
4. E se con partenza in A1 e arrivo in G9 al robot viene richiesto di passare per la cella D5? (1 punto)
