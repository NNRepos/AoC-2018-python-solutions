import sys
import re
import operator as op
input="""\
#ip 4
seti 123 0 5
bani 5 456 5
eqri 5 72 5
addr 5 4 4
seti 0 0 4
seti 0 7 5
bori 5 65536 3
seti 733884 6 5
bani 3 255 1
addr 5 1 5
bani 5 16777215 5
muli 5 65899 5
bani 5 16777215 5
gtir 256 3 1
addr 1 4 4
addi 4 1 4
seti 27 8 4
seti 0 6 1
addi 1 1 2
muli 2 256 2
gtrr 2 3 2
addr 2 4 4
addi 4 1 4
seti 25 4 4
addi 1 1 1
seti 17 8 4
setr 1 7 3
seti 7 0 4
eqrr 5 0 1
addr 1 4 4
seti 5 9 4""" 
try: #funcs
  def addr(A,B,C,regs):
    regs[C]=regs[A]+regs[B]
    return regs
  def addi(A,B,C,regs):
    regs[C]=regs[A]+B
    return regs
  def mulr(A,B,C,regs):
    regs[C]=regs[A]*regs[B]
    return regs
  def muli(A,B,C,regs):
    regs[C]=regs[A]*B
    return regs
  def banr(A,B,C,regs):
    regs[C]=regs[A]&regs[B]
    return regs
  def bani(A,B,C,regs):
    regs[C]=regs[A]&B
    return regs
  def borr(A,B,C,regs):
    regs[C]=regs[A]|regs[B]
    return regs
  def bori(A,B,C,regs):
    regs[C]=regs[A]|B
    return regs
  def setr(A,B,C,regs):
    regs[C]=regs[A]
    return regs
  def seti(A,B,C,regs):
    regs[C]=A
    return regs
  def gtir(A,B,C,regs):
    regs[C]=1 if A>regs[B] else 0
    return regs
  def gtri(A,B,C,regs):
    regs[C]=1 if regs[A]>B else 0
    return regs
  def gtrr(A,B,C,regs):
    regs[C]=1 if regs[A]>regs[B] else 0
    return regs
  def eqir(A,B,C,regs):
    regs[C]=1 if A==regs[B] else 0
    return regs
  def eqri(A,B,C,regs):
    regs[C]=1 if regs[A]==B else 0
    return regs
  def eqrr(A,B,C,regs):
    regs[C]=1 if regs[A]==regs[B] else 0
    return regs
except Exception as e:
  print "in funcs:",str(e),sys.exc_info()[2].tb_lineno
  raw_input()
try: #main
  #vars
  input=[i.split() for i in input.split('\n')] #funcs
  funcDict={}
  funcs=["addr","addi","mulr","muli","banr","bani","borr","bori",\
         "setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]
  for f in funcs:
    funcDict[f]=locals()[f]
  # funcs2=[locals()[i] for i in funcs]
  instructions=input[1:]
  instructions=[[ins[0]]+map(int,ins[1:]) for ins in instructions]
  ip=int(input[0][1])
  regs=[0]*6
  insCount=len(instructions)
  while regs[ip]>=0 and regs[ip]<insCount:
    func,A,B,C=instructions[regs[ip]]
    print "b4:",regs
    instruct=instructions[regs[ip]]
    print "instruct:", instruct
    if regs[ip]==28:
      print "r5==r0:",regs[5]
      raw_input()
    regs=funcDict[func](A,B,C,regs)
    regs[ip]+=1
    print "after:", regs
    raw_input()
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()