import sys
import re
import operator as op
input="""\
|....|....||.##|.|.|.##.|....|..#|#|#.#|.#|#|....#
.#...#.#....#|..#.#||........|.#.#.###.|.#||##..#.
....|..#####...|.##.#.|.|.|||.|#...|..|....##|#.||
|..#..|..#|#|.....#..|.....#........#....|..#..#..
..#|##..##..#.........|##.|..#.|.|....|#.||#.##...
.......|...|#..####.|#..#.||...|#.......|..|.|.#|#
....|||............|..#|.#..|.|.|...|...........|.
.|##.|.|...#...|||..#.#.##.|.#.|..||#.#....#......
.#..#|....#...#.#..|..#.#...#..|#||....#...#||#..#
#|...||.|#.#.|..##|..#..|......|..|....|#.|##.....
#.#|...##.|..##...||#.|..#|.|..|.|..#....#....#|..
##|||...##.....#|..||.||..|...#.###|.#..#.#..||.##
#|.|...|#...#..#.........#..#.##..#.|##.|.|.#####.
#.#..|.#.#.#|...#....|.|##.|....#..|#....|.#.#....
........|##.|...|...|....#..#..|..|#....#..#|#.|..
...#|.|.......||.|..#..|..#....|||#|.|........|##.
...##|.....|...|.#|.|.|.#|..##|..|#...#|||..#.#.|.
...|...#..|....#...###||##..|..#|.|..##|.#.||.....
...........#.|#..#.#|.|.#.#.......||.#..|.....#..#
.#..#.#....#|.|###...##..#.##|.|#..|....|#....#|.#
.#|....|.|..#..#.....#.#.|...#.....||.|.......#|.#
.|#...#.##...||||.#..#.....|#.||#.#....#|#...#|...
..#...#.#.|...#|.......#|##|.|.#.||.#|.#...|#.....
.......#....###|....||......|....|.....##.|.|.|...
|.|.|.|.#.#..##......#..|..##.#....#.#|....#.|..#.
.|...||...#.##..#..||...##..|.|.#.#.|.|....#......
....|......|..|.|.##.#.|.#.||........|.|#|.#.|..#.
.#.#...#...||..|.......||#.#|..|#||||..#|......|..
|||#.|#.|.##.#....#.#.|||||.....||.||.||.#|.##|#.#
........#|.|##..##.|......#||.|.#......#.....##.##
..||..#|.|.#..|#...#.....|..|#.||.#.|#.|#...#.|...
|#..#...|....|.........|.|##.#..#|##||#...#..#.|#.
...##..#.#..#|...#.|##...#....#....#|...#|..|.|.#.
.#|.......#|.||#..||#.#..|#.|.|..#.#..|..|..#..|..
#.|#.#|...|.#.#|..#..|...|#||#|.|#........|....|..
|.|||.|.|##||...|.|#..#|||.#.###||.#|.###...#....#
.##....#..|#.........#.|..|..||.#|..#|##|.#.....##
.....|#.#...|....#......||..|...|...#.....#.||..##
#|.|#..##.....|##....|.#.#.||.|.......||#.#.#..|#.
.#...#|.#.#||...|#..##.|..##.|.#|.||##.|.......||.
.|...#..|..#.##.#|||#####|.|....|#..###.|#.#..|.#|
...##.....||..|......|.#|.|.|.|.|..#.......##.|#..
|...|..|.#|..#|##.##...|.#|.#|#.......|.#.|#||.|..
.|..######......#|.#...#.#.|.#|...#..|....|..|..||
|#.#.#..|.|#|....##.||....#...#..|....#.|||.|##.|.
#|...#.#||..|...|.....###|.#....#|....|#...|..#.#.
..#|.||..#..#.......##...#|..#.##..#....||.|.|.##|
.||#.##.###..#|...........#....#|.#..#.##.|#.#...#
.##|##..#.|#.|......#..|#...#.....#.|.|#|...|.|...
..#.....##..#.#|#.#.....|#...#..|.#.|.|#|....#..|.""" 
try:
  input=[list(i) for i in input.split('\n')]
  forest=input
  openChar=r'.'
  treeChar=r'|'
  lumberChar=r'#'
  Ysize=len(forest)
  Xsize=len(forest[0])
  generations=1000000000
  def isValid(x,y):
    if x>-1 and x<Xsize and y>-1 and y<Ysize:
      return True
  def aroundPoint(x,y):
    ret=[]
    if isValid(y,x+1):
      ret.append(forest[y][x+1])
    if isValid(y,x-1):
      ret.append(forest[y][x-1])
    if isValid(y+1,x):
      ret.append(forest[y+1][x])
    if isValid(y-1,x):
      ret.append(forest[y-1][x])
    if isValid(y-1,x-1):
      ret.append(forest[y-1][x-1])
    if isValid(y-1,x+1):
      ret.append(forest[y-1][x+1])
    if isValid(y+1,x-1):
      ret.append(forest[y+1][x-1])
    if isValid(y+1,x+1):
      ret.append(forest[y+1][x+1])
    return ret
    
  #...
  counts=[0]
  flag=False
  for gen in xrange(generations):
    if flag:
      break;
    newForest=[]
    for row in range(Ysize): #run over forest
      newRow=[]
      for col in range(Xsize): #run over row 
        ch=forest[row][col]
        ar=aroundPoint(col,row)
        if ch==openChar:
          if ar.count(treeChar)>=3:
            newRow.append(treeChar)
          else:
            newRow.append(openChar)
        elif ch==treeChar:
          if ar.count(lumberChar)>=3:
            newRow.append(lumberChar)
          else:
            newRow.append(treeChar)
        else:
          if ar.count(lumberChar)>=1 and ar.count(treeChar)>=1:
            newRow.append(lumberChar)
          else:
            newRow.append(openChar)
      newForest.append(newRow)
    forest=newForest
    treeCount=sum([ i.count(treeChar) for i in forest])
    lumberCount=sum([ i.count(lumberChar) for i in forest])
    pair=[treeCount,lumberCount]
    countL=len(counts)
    for somePair in range(5, countL):
      if counts[somePair]==pair:
        if counts[somePair-1]==counts[countL-1]:
          if counts[somePair-2]==counts[countL-2]:
            print "3 reps found at",somePair-2,"-",somePair,\
            "and",countL-2,"-",countL
            flag=True
            break;
    counts.append(pair)
  genDiff=countL-somePair
  rotations=((generations-somePair)/genDiff)
  print "r",rotations
  repeatingPairGen=generations- rotations*genDiff
  finalAns=counts[repeatingPairGen][0]*counts[repeatingPairGen][1]
  print "Since the repetition occured in", genDiff, "generations,\
  \nwe can induce that the",str(generations)+"th generation will produce the same pair\
 as the", str(repeatingPairGen) + "th generation.\nHence, the final answer is",finalAns
except Exception as e:
  print str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()