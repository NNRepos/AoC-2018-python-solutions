r0=int(raw_input("reg 0="))
r1=r2=r3=r4=r5=0
r5=123 #0
while r5!=72: #2,3,4
  r5=r5&456 #1
r5=0 #5
while(True): #30
  r3=r5|65536 #6
  r5=733884 #7
  while(True): #27,16
    r1=r3&255 #8 #means r1=r3%256
    r5+=r1 #9
    r5&=16777215 #10 #means r5%=16777216
    r5*=65899 #11
    r5&=16777215 #12 #means r5%=16777216
    if 256>r3: #13,14,15
      print r5 #value compared to r0
      raw_input()
      if r5==r0: #16,28
        exit() #29
      else:
        break #30
    else: 
      r1=0 #17
      r2=1 #18
      while r2<=r3: #20,21,22,23,25 #r3=r3/256
        r2=r1+1 #18
        r2*=256 #19
        r1+=1 #24
      r3=r1-1 #26