import sys
import re
import operator as op
input="""\
81, 46
330, 289
171, 261
248, 97
142, 265
139, 293
309, 208
315, 92
72, 206
59, 288
95, 314
126, 215
240, 177
78, 64
162, 168
75, 81
271, 258
317, 223
210, 43
47, 150
352, 116
316, 256
269, 47
227, 343
125, 290
245, 310
355, 301
251, 282
353, 107
254, 298
212, 128
60, 168
318, 254
310, 303
176, 345
110, 109
217, 338
344, 330
231, 349
259, 208
201, 57
200, 327
354, 111
166, 214
232, 85
96, 316
151, 288
217, 339
62, 221
307, 68""" 
try:
  #find max coordinate
  max_x, max_y = 0,0
  input=input.split('\n')
  input = [[int(i) for i in j.split(', ')] for j in input]
  for i in input:
    x,y = i
    max_x, max_y = max(x+5,max_x),max(y+5,max_y)
  #fill grid
  grid = [[0]*max_x for i in range(max_y)]
  for x in range(max_x):
    if not x%(max_x/5) and not x==0:
      print str(100*x/max_x) + "%"
    for y in range(max_y):
      minDist=max_x + max_y; 
      for a,i in enumerate(input):
        if abs(i[0]-x) + abs(i[1]-y) < minDist:
          minDist=abs(i[0]-x) + abs(i[1]-y)
          grid[y][x]=[a, minDist]
        elif abs(i[0]-x) + abs(i[1]-y) == minDist:
          grid[y][x]='.'
  blocks=dict()
  #count grid
  for x in range(max_x):
    for y in range(max_y):
      if grid[y][x] == 0:
        pass
      elif grid[y][x] == '.':
        pass
      else:
        target = grid[y][x][0]
        if target not in blocks:
          blocks[target]=1
        else:
          blocks[target]+=1
  #remove infinities
  for y in range(1,max_y):
    a=grid[y][0][0]
    b=grid[y][max_x-1][0]
    blocks[a]=0
    blocks[b]=0
  for x in range(1,max_x):
    a=grid[0][x][0]
    b=grid[max_y-1][x][0]
    blocks[a]=0
    blocks[b]=0
  print "highest is",max(blocks.values())
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()