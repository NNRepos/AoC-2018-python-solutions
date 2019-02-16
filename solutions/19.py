import sys
import re
import operator as op
input="""\
#ip 5
addi 5 16 5
seti 1 1 2
seti 1 8 1
mulr 2 1 3
eqrr 3 4 3
addr 3 5 5
addi 5 1 5
addr 2 0 0
addi 1 1 1
gtrr 1 4 3
addr 5 3 5
seti 2 6 5
addi 2 1 2
gtrr 2 4 3
addr 3 5 5
seti 1 2 5
mulr 5 5 5
addi 4 2 4
mulr 4 4 4
mulr 5 4 4
muli 4 11 4
addi 3 2 3
mulr 3 5 3
addi 3 13 3
addr 4 3 4
addr 5 0 5
seti 0 8 5
setr 5 5 3
mulr 3 5 3
addr 5 3 3
mulr 5 3 3
muli 3 14 3
mulr 3 5 3
addr 4 3 4
seti 0 9 0
seti 0 9 5""" 
try:
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
    regs=funcDict[func](A,B,C,regs)
    regs[ip]+=1
  print "final answer:",regs[0]
except Exception as e:
  print "in main:",str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()