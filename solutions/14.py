import sys
import re
import operator as op
input="""\
074501""" 
try:
  target=int(input)
  extra=10
  currA=0
  currB=1
  recipes=[3,7]
  while(len(recipes)<(target+extra)):
    currSum=recipes[currA]+recipes[currB]
    if currSum>9:
      recipes.append(currSum/10)
      recipes.append(currSum%10)
    else:
      recipes.append(currSum)
    newlen=len(recipes)
    currA=(currA+recipes[currA]+1)%newlen
    currB=(currB+recipes[currB]+1)%newlen
  print "The last recipes are:", ''.join(map(str,recipes[target:target+extra]))
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()