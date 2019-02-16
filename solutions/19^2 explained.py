try:
  r0,r1,r2,r4,r5 = 0, 1, 0, 10551293, 1

  while(True):
    r1=1
    while (True):
      if r2*r1==r4:
        r0+=r2
      r1+=1
      if r1>r4:
        r2+=1
        if r2>r4:
          raise Exception("ip out of range")
        else:
          break;
except Exception:
  print r0
finally:
  raw_input()