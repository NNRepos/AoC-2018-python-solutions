import sys
import re
import operator as op
input="""\
074501""" 
try:
  target=int(input)
  tarLen=len(input)
  extra=10
  currA=0
  currB=1
  recipes=[3,7]
  currLen=2
  printed=False
  while(8):
    if currLen%(1000*1000)<2 and not printed:
      print currLen-currLen%(1000*1000), "recipes done"
      printed=True
    else:
      printed=False
    currSum=recipes[currA]+recipes[currB]
    if currSum>9:
      recipes.append(currSum/10)
      recipes.append(currSum%10)
      currLen+=2
    else:
      recipes.append(currSum)
      currLen+=1
    currA=(currA+recipes[currA]+1)%currLen
    currB=(currB+recipes[currB]+1)%currLen
    temp=recipes[-tarLen-1:]
    temp=map(str,temp)
    if(str(''.join((temp[-tarLen:])))==str(input)):
      print "found target in",len(recipes)-tarLen,"recipes"
      break
    elif(str(''.join((temp[-tarLen-1:-1])))==str(input)):
      print "found target in",len(recipes)-tarLen-1,"recipes"
      break
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()