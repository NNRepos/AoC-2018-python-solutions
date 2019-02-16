r0=0
r5=0
values=[]
while(True):
  r3=r5|65536 #6
  r5=733884 #7
  while(True): #27,16
    r5=((r5 + r3%256)*65899)%16777216
    if 256>r3: #13,14,15
      if r5 in values:
        print "repetition found, newest value is",values[-1]
        raw_input()
        raise Exception("done")
      values.append(r5)
      # print "values found:",len(values)
      if r5==r0: #16,28
        exit() #29
      else:
        break #30
    else: 
      r3/=256