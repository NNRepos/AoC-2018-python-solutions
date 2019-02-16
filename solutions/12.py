import sys
import re
import operator as op
input="""\
initial state: ##.#.#.##..#....######..#..#...#.#..#.#.#..###.#.#.#..#..###.##.#..#.##.##.#.####..##...##..#..##.#.

...## => #
#.#.# => #
.###. => #
#.#.. => .
.#..# => #
#..#. => #
..##. => .
....# => .
#.... => .
###.. => #
.#### => #
###.# => .
#..## => #
..... => .
##.## => #
####. => .
##.#. => .
#...# => .
##### => .
..#.. => .
.#.#. => .
#.### => .
.##.# => .
..#.# => .
.#.## => #
...#. => .
##... => #
##..# => #
.##.. => .
.#... => #
#.##. => #
..### => .""" 
try:
  #parse input
  minX=0
  generations=20
  input = input.split('\n')
  init = list(input[0].split()[2])
  curr=init
  rules=[]
  for i in range (2,len(input)):
    i=input[i].split()
    rules.append([i[0],i[2]])
  #tick
  for i in range(generations):
    currSize=len(curr)
    #find new list size
    startX=max(0,4-curr.index('#'))
    minX-=startX;
    endX=max(0, 4-list(reversed(curr)).index('#'))
    #init new list
    curr=['.']*startX+curr[:]+['.']*endX
    newSize=len(curr)
    newCurr=['.']*2
    #go over rules
    for j in range(2, newSize-2):
      string=''.join(curr[j-2:j+3])
      for k in rules:
        if k[0]==string:
          newCurr.append(k[1])
          break;
      else:
        raise("rule not found")
    newCurr+=['.']*2
    curr=newCurr
  #sum plants
  sumPlants=0
  for i, plant in enumerate(curr):
    if plant=='#':
      sumPlants+=i+minX
  print "The sum is:", sumPlants
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()