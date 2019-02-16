try:
  r0,r1,r2,r4,r5 = 0, 1, 0, 10551293, 1
  target = int(__import__('math').sqrt(r4))
  for i in range (1,target+1):
    if not r4%i:
      j=r4/i
      if i==j:
        r0+=i
      else:
        r0+=i+j
  print "final answer:",r0
except Exception:
  print r0
finally:
  raw_input()