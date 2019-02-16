import sys
import re
import operator as op
input="""\
depth: 5616
target: 10,785""" 
# input="""\
# depth: 510
# target: 10,10"""
try:
  #classes
  class PriorityQueue:
    def __init__(self):
      self.queue=[]
      self.counter=0
    
    def worseThan(self, position, new_list):
      """checks if item in given position is worse than new_list"""
      thisCost= self.queue[position][0] + heuristic(self.queue[position][1])
      newCost= new_list[0] + heuristic(new_list[1])
      if thisCost>newCost: #check cost
        return True
      elif thisCost==newCost:
        if self.queue[position][3]>new_list[3]: #check counter
          return True
      return False
    
    def display(self):
      print "printing queue with heuristic:"
      for i in range(len(self.queue)):
        if self.queue[i][1]==[targetX,targetY]:
          print "TARGET:"
        print self.queue[i][0]+heuristic(self.queue[i][1]), self.queue[i]
    
    def isEmpty(self):
      if len(self.queue)<1:
        return True
    
    def add(self,list_with_cost): #should receive [cost_so_far, location, tool]
      cost_so_far, location, tool = list_with_cost
      self.counter+=1
      push_me=[cost_so_far, location, tool, self.counter]
      if self.isEmpty():
        self.queue[0:0]=[push_me]
        return
      low,high=0,len(self.queue)-1
      while low<high-1:
        mid=(low+high)/2
        if self.worseThan(mid, push_me):
          high=mid-1
        else:
          low=mid+1
      #remember - the better cost should be lower in the PriorityQueue.
      if self.worseThan(low, push_me): #push_me is better than low and replaces it
        self.queue[low:low]=[push_me]
      elif not self.worseThan(high, push_me): #push_me is worse than high and comes above it
        self.queue[high+1:high+1]=[push_me]
      else: #push_me is between low and high and replaces high
        self.queue[high:high]=[push_me]
    
    def pop(self):
      return self.queue.pop(0)
  #funcs
  def switchTool(curr,region):
    if region==0: #rocky can use torch or climbing
      if curr==0:
        return 1
      elif curr==1:
        return 0
      else:
        raise Exception("bad tool")
    elif region==1: #wet can use climbing or neither
      if curr==1:
        return 2
      elif curr==2:
        return 1
      else:
        raise Exception("bad tool")
    elif region==2: #narrow can use torch or neither
      if curr==0:
        return 2
      elif curr==2:
        return 0
      else:
        raise Exception("bad tool")
    else:
      raise Exception("bad region")
  
  
  def isValid(x,y,tool):
    if x>=0 and x<=maxX and y>=0 and y<=maxY:
      tool1=tool
      tool2=((tool-1) % 3)
      if cave[y][x] in [tool1, tool2]:
        return True
  
  
  def changeMinDist(x,y,tool,val):
    minimal_distances[tool][y][x] = val
  
  
  def heuristic(location):
    x,y,xx,yy=location[0], location[1], targetX, targetY
    return abs(x-xx) + abs(y-yy)
  
  
  def rescue(x,y,mins,tool):
    """use A* algorithm to find santa's friend"""
    global min_time_to_target
    rounds=0
    pq=PriorityQueue()
    pq.add([mins,[x,y],tool]) #pq items look like this: [cost, [coordinates], tool, counter]
    while not pq.isEmpty():
      rounds+=1
      curr_visit=pq.pop()
      cost, location, currTool, _= curr_visit
      currX,currY=location
      otherTool=switchTool(currTool, cave[currY][currX])
      if (location == [targetX, targetY]): #found buddy
        if minimal_distances[0][targetY][targetX]!=-1 and minimal_distances[0][targetY][targetX] < min_time_to_target:
          min_time_to_target=minimal_distances[0][targetY][targetX]
        if minimal_distances[1][targetY][targetX]!=-1 and minimal_distances[1][targetY][targetX]+7 < min_time_to_target:
          min_time_to_target=minimal_distances[1][targetY][targetX]+7
      else: #didn't find buddy
        #add neighbours with their cost and tool
        if isValid(currX+1, currY, currTool): #go right with same tool
          if cost+1<minimal_distances[currTool][currY][currX+1] or minimal_distances[currTool][currY][currX+1]==-1:
            pq.add([cost+1, [currX+1,currY], currTool])
            changeMinDist(currX+1, currY, currTool, cost+1)
        if isValid(currX+1, currY, otherTool): #go right with diff tool
          if cost+8<minimal_distances[otherTool][currY][currX+1] or minimal_distances[otherTool][currY][currX+1]==-1:
            pq.add([cost+8, [currX+1,currY], otherTool])
            changeMinDist(currX+1, currY, otherTool, cost+8)
        
        if isValid(currX, currY+1, currTool): #go down with same tool
          if cost+1<minimal_distances[currTool][currY+1][currX] or minimal_distances[currTool][currY+1][currX]==-1:
            pq.add([cost+1, [currX,currY+1], currTool])
            changeMinDist(currX, currY+1, currTool, cost+1)
        
        if isValid(currX, currY+1, otherTool): #go down with diff tool
          if cost+8<minimal_distances[otherTool][currY+1][currX] or minimal_distances[otherTool][currY+1][currX]==-1:
            pq.add([cost+8, [currX,currY+1], otherTool])
            changeMinDist(currX, currY+1, otherTool, cost+8)
        
        if isValid(currX-1, currY, currTool): #go left with same tool
          if cost+1<minimal_distances[currTool][currY][currX-1] or minimal_distances[currTool][currY][currX-1]==-1:
            pq.add([cost+1, [currX-1,currY], currTool])
            changeMinDist(currX-1, currY, currTool, cost+1)
        
        if isValid(currX-1, currY, otherTool): #go left with diff tool
          if cost+8<minimal_distances[otherTool][currY][currX-1] or minimal_distances[otherTool][currY][currX-1]==-1:
            pq.add([cost+8, [currX-1,currY], otherTool])
            changeMinDist(currX-1, currY, otherTool, cost+8)
        if isValid(currX, currY-1, currTool): #go up with same tool
          if cost+1<minimal_distances[currTool][currY-1][currX] or minimal_distances[currTool][currY-1][currX]==-1:
            pq.add([cost+1, [currX,currY-1], currTool])
            changeMinDist(currX, currY-1, currTool, cost+1)
        
        if isValid(currX, currY-1, otherTool): #go up with diff tool
          if cost+8<minimal_distances[otherTool][currY-1][currX] or minimal_distances[otherTool][currY-1][currX]==-1:
            pq.add([cost+8, [currX,currY-1], otherTool])
            changeMinDist(currX, currY-1, otherTool, cost+8)
  
  
  #vars
  input=[ list(re.split(',| ',row)) for row in input.split('\n')]
  depth=int(input[0][1])
  targetX,targetY=map(int,input[1][1:])
  maxX,maxY=targetX+100,targetY+100
  rockyChar=r'.'
  wetChar=r'='
  narrowChar=r'|'
  chars=[rockyChar,wetChar,narrowChar]
  tools=["torch", "climbing gear", "neither"]
  min_time_to_target=123123123 #arbitrary large number
  #main
  #fill cave with types - part 1
  print "creating cave map..."
  cave=[ [0]*(maxX+1) for y in range(maxY+1)] #init cave
  for r,row in enumerate(cave): #fill cave with erosion
    for c,col in enumerate(row):
      #get geologic index
      if c==targetX and r==targetY:
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
  for r,row in enumerate(cave): #fill cave with tool numbers
    for c,col in enumerate(row):
      cave[r][c]=cave[r][c] % 3
  #rescue buddy - part 2
  #create minimal distance for each tool
  print "rescuing buddy..."
  minimal_distances=[]
  minimal_distances.append([ [-1]*(maxX+1) for y in range(maxY+1)]) #init torch
  minimal_distances.append([ [-1]*(maxX+1) for y in range(maxY+1)]) #init climbing
  minimal_distances.append([ [-1]*(maxX+1) for y in range(maxY+1)]) #init neither
  changeMinDist(0,0,0,0) #starting region is torch
  rescue(0,0,0,0)
  print "the shortest time is", min_time_to_target, "minutes."
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()