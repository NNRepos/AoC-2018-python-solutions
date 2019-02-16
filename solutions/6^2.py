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
  grid = [[0]*1000 for i in range(1000)]
  input=input.split('\n')
  input = [[int(i) for i in j.split(', ')] for j in input]
  regionSize=0;
  for i in range(1000):
    if not i%100 and not i==0:
      print str(i/10) + "%"
    for j in range(1000):
      dist=0;
      for k in input:
        dist+=abs(i-k[0])+abs(j-k[1]);
      if dist<10000:
        regionSize+=1;
  print "region size is:", regionSize
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()