import sys
import re
import operator as op
input="""\
depth: 5616
target: 10,785""" 
try:
  #funcs
  
  #vars
  input=[ list(re.split(',| ',row)) for row in input.split('\n')]
  depth=int(input[0][1])
  maxX,maxY=map(int,input[1][1:])
  rockyChar=r'.'
  wetChar=r'='
  narrowChar=r'|'
  risk=0
  #main
  cave=[ [0]*(maxX+1) for y in range(maxY+1)]
  for r,row in enumerate(cave):
    for c,col in enumerate(row):
      #get geologic index
      if c==maxX and r==maxY:
        gindex=0
      elif c==0:
        gindex=r*48271
      elif r==0:
        gindex=c*16807
      else:
        gindex=(cave[r-1][c])*(cave[r][c-1])
      #erosion
      erosion=(gindex+depth)%20183
      cave[r][c]=erosion
      risk+=erosion%3
  print "the total risk is:",risk
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()