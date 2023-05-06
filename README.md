# Noughts and crosses

Inspired by reading Rodnay Zaks' 1980 book '6502 Games', I thought I'd have a go at coding some simple noughts and crosses ('tic tac toe') games in Python, as I don't think I've ever done this simple thing before.

There are doubtless much more elegant and compact ways of coding this, I just did this for a bit of fun and relaxation, and I think I've made three incrementally clever versions which a student could follow and improve upon.

## How to play

In all versions, you make your move by entering the square number:
```
012
345
678
```

## ox.py

ox.py is just a game for 2 human players, so I could set up a simple user interface that spots when a player has won or if it's a draw.



## ox2.py

ox2.py is a game you play against the computer, but the human always goes first and the computer just picks the first free square, so it's super easy to beat.

## ox3.py

ox3.py uses something closer to Zaks' algorithm:

- You can choose who plays first, human or computer
- The computer scans each row, column and diagonal and assigns a weighting score to each square:
  - Squares already played get a weight of 0
  - Playable squares get a weight of 1
  - Potential winning squares get an extra weight of 6
  - Potential losing squares, in which the human could win, get an extra weight of 5
  - Squares in an otherwise empty line where the human has placed a O get an extra weighting of 1

The program then picks the square with the highest weighting number for its move. It also prints out its scoring array and thinking about threats and possible winning squares, so you can follow how it has made its choice.

It's not very imaginative, there's no random element and if there are multiple squares with the same high weigting score, it will always pick the first square suggested by the algorithm.
