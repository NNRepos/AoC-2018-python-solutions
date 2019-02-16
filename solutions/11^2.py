import sys
import re
import operator as op
input="""\
5153""" 
try:
  input=int(input)
  gridStart=1
  gridEnd=301
  def calc_power(x,y):
    if not x < gridEnd:
      return 0
    if not y < gridEnd:
      return 0
    ret=0
    ret= ((((((x+10)*y)+input)*(x+10)) %1000)/100)-5
    return ret
  #calc grid
  grid=[list(range(gridStart,gridEnd)) for i in range(gridStart,gridEnd)]
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      grid[row][col]=calc_power(col+gridStart, row+gridStart)
  #begin searching
  maxS=0
  bestXYZ=[]
  for squareSize in range(1,18):
    print "searching size", squareSize
    for row in range(len(grid)-(squareSize-1)):
      for col in range(len(grid[0])-(squareSize-1)):
        s=0
        for Arow in range(squareSize):
          for Acol in range(squareSize):
            s+=grid[row+Arow][col+Acol]
        if s>maxS:
          maxS=s
          bestXY=[col+1, row+1, squareSize]
  #done
  answer=','.join(map(str,bestXY))
  print "x,y,size coordinates are:", bestXY
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()