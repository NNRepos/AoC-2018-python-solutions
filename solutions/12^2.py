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
  sums=[]
  minX=0
  generations=50*1000*1000*1000
  input = input.split('\n')
  init = list(input[0].split()[2])
  curr=init
  rules=[]
  for i in range (2,len(input)):
    i=input[i].split()
    rules.append([i[0],i[2]])
  #tick
  for i in range(666666):
    # if not i%(generations/100):
      # print i*100/generations, "%done"
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
    for j, plant in enumerate(curr):
      if plant=='#':
        sumPlants+=j+minX
    strCurr=''.join(curr).strip('.')
    for j,sumPair in enumerate(sums):
      if strCurr==sumPair[0]:
        print "The",i+1, "sum is:", sumPlants
        genDiff=i-j;
        sumDiff=sumPlants-sumPair[1]
        print "So every",genDiff,"generations, the sum changes by",sumDiff
        targetGen=j+1
        repetitions=(generations-targetGen)/float(genDiff)
        print "We can conclude that the pattern will repeat", int(repetitions),\
        "times, until generation", targetGen, "will match the last generation"
        ans=int(sums[j][1]+repetitions*sumDiff)
        print "The final answer is:", ans
        raw_input()
        raise Exception("repetition found, exiting")
    sums.append([strCurr,sumPlants])
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()