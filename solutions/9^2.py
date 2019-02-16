import sys
import re
import operator as op
from collections import deque
input="""\
428 players; last marble is worth 70825 points""" 
try:
  marbles=deque([0])
  players=428
  playerScore=[0]*players
  lastMarble=70825*100
  for m in range(1,lastMarble):
    currPlayer=m%players
    if not m%23:
      playerScore[currPlayer]+=m;
      marbles.rotate(7)
      playerScore[currPlayer]+=marbles.pop()
      marbles.rotate(-1)
    else:
      marbles.rotate(-1)
      marbles.append(m)
  print max(playerScore)
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()