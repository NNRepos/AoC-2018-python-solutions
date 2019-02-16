import sys
import re
import operator as op
input="""\
Before: [3, 1, 2, 0]
5 1 2 0
After:  [0, 1, 2, 0]

Before: [3, 3, 0, 2]
10 2 0 1
After:  [3, 0, 0, 2]

Before: [3, 3, 1, 1]
7 3 3 3
After:  [3, 3, 1, 0]

Before: [1, 3, 2, 0]
8 0 2 2
After:  [1, 3, 0, 0]

Before: [3, 0, 0, 2]
12 2 3 2
After:  [3, 0, 1, 2]

Before: [0, 3, 1, 1]
1 2 3 1
After:  [0, 2, 1, 1]

Before: [1, 1, 0, 2]
2 0 2 2
After:  [1, 1, 0, 2]

Before: [3, 1, 3, 3]
0 1 2 0
After:  [0, 1, 3, 3]

Before: [3, 0, 2, 1]
10 1 0 3
After:  [3, 0, 2, 0]

Before: [2, 1, 3, 0]
14 0 3 0
After:  [1, 1, 3, 0]

Before: [1, 0, 0, 3]
2 0 2 1
After:  [1, 0, 0, 3]

Before: [2, 1, 3, 0]
0 1 2 3
After:  [2, 1, 3, 0]

Before: [2, 1, 0, 0]
14 0 3 0
After:  [1, 1, 0, 0]

Before: [2, 1, 2, 1]
4 3 1 2
After:  [2, 1, 0, 1]

Before: [1, 0, 1, 1]
7 3 3 1
After:  [1, 0, 1, 1]

Before: [0, 1, 0, 1]
7 3 3 2
After:  [0, 1, 0, 1]

Before: [0, 1, 3, 2]
0 1 2 1
After:  [0, 0, 3, 2]

Before: [1, 1, 2, 2]
8 0 2 3
After:  [1, 1, 2, 0]

Before: [2, 0, 2, 2]
10 1 0 0
After:  [0, 0, 2, 2]

Before: [2, 1, 3, 1]
0 1 2 3
After:  [2, 1, 3, 0]

Before: [1, 1, 2, 2]
8 0 2 1
After:  [1, 0, 2, 2]

Before: [0, 0, 2, 1]
11 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 0, 2, 0]
3 2 2 0
After:  [4, 0, 2, 0]

Before: [1, 0, 0, 0]
2 0 2 3
After:  [1, 0, 0, 0]

Before: [2, 0, 0, 1]
4 0 1 1
After:  [2, 1, 0, 1]

Before: [2, 0, 3, 3]
10 1 0 3
After:  [2, 0, 3, 0]

Before: [0, 1, 3, 2]
0 1 2 0
After:  [0, 1, 3, 2]

Before: [2, 1, 3, 3]
0 1 2 3
After:  [2, 1, 3, 0]

Before: [0, 1, 2, 1]
11 3 2 3
After:  [0, 1, 2, 1]

Before: [0, 2, 2, 3]
13 0 2 1
After:  [0, 0, 2, 3]

Before: [0, 2, 3, 2]
13 0 1 3
After:  [0, 2, 3, 0]

Before: [1, 1, 2, 2]
4 3 2 1
After:  [1, 0, 2, 2]

Before: [1, 1, 2, 1]
11 3 2 2
After:  [1, 1, 1, 1]

Before: [0, 2, 1, 0]
13 0 1 1
After:  [0, 0, 1, 0]

Before: [2, 1, 2, 2]
9 2 0 0
After:  [1, 1, 2, 2]

Before: [1, 1, 1, 1]
1 2 0 3
After:  [1, 1, 1, 2]

Before: [3, 3, 0, 2]
12 2 3 2
After:  [3, 3, 1, 2]

Before: [0, 1, 2, 2]
3 3 2 1
After:  [0, 4, 2, 2]

Before: [0, 2, 2, 3]
13 0 3 0
After:  [0, 2, 2, 3]

Before: [1, 3, 1, 0]
1 2 0 0
After:  [2, 3, 1, 0]

Before: [0, 1, 1, 3]
15 1 3 3
After:  [0, 1, 1, 0]

Before: [3, 2, 3, 0]
12 3 2 3
After:  [3, 2, 3, 1]

Before: [1, 0, 1, 3]
1 2 0 3
After:  [1, 0, 1, 2]

Before: [3, 1, 2, 1]
11 3 2 2
After:  [3, 1, 1, 1]

Before: [0, 0, 0, 2]
6 0 0 3
After:  [0, 0, 0, 0]

Before: [1, 0, 0, 1]
2 0 2 3
After:  [1, 0, 0, 0]

Before: [0, 3, 0, 2]
6 0 0 0
After:  [0, 3, 0, 2]

Before: [1, 1, 3, 0]
0 1 2 0
After:  [0, 1, 3, 0]

Before: [3, 1, 0, 3]
15 1 3 0
After:  [0, 1, 0, 3]

Before: [3, 2, 0, 2]
10 2 0 1
After:  [3, 0, 0, 2]

Before: [0, 2, 0, 2]
6 0 0 1
After:  [0, 0, 0, 2]

Before: [0, 3, 3, 1]
6 0 0 1
After:  [0, 0, 3, 1]

Before: [0, 1, 2, 0]
3 2 2 3
After:  [0, 1, 2, 4]

Before: [3, 0, 0, 0]
4 0 2 1
After:  [3, 1, 0, 0]

Before: [0, 2, 2, 1]
11 3 2 3
After:  [0, 2, 2, 1]

Before: [2, 0, 3, 3]
9 3 2 0
After:  [1, 0, 3, 3]

Before: [2, 1, 2, 2]
5 1 2 2
After:  [2, 1, 0, 2]

Before: [1, 1, 2, 2]
5 1 2 2
After:  [1, 1, 0, 2]

Before: [0, 1, 0, 1]
6 0 0 3
After:  [0, 1, 0, 0]

Before: [1, 3, 2, 2]
3 2 2 1
After:  [1, 4, 2, 2]

Before: [3, 0, 2, 2]
3 2 2 2
After:  [3, 0, 4, 2]

Before: [2, 1, 2, 1]
3 2 2 0
After:  [4, 1, 2, 1]

Before: [1, 3, 2, 3]
8 0 2 2
After:  [1, 3, 0, 3]

Before: [2, 1, 1, 3]
4 2 1 0
After:  [0, 1, 1, 3]

Before: [2, 0, 1, 1]
1 2 3 0
After:  [2, 0, 1, 1]

Before: [3, 0, 0, 3]
10 1 0 0
After:  [0, 0, 0, 3]

Before: [1, 1, 3, 1]
0 1 2 1
After:  [1, 0, 3, 1]

Before: [0, 0, 1, 2]
6 0 0 2
After:  [0, 0, 0, 2]

Before: [3, 3, 0, 2]
10 2 0 2
After:  [3, 3, 0, 2]

Before: [2, 3, 2, 1]
11 3 2 0
After:  [1, 3, 2, 1]

Before: [1, 0, 0, 1]
2 0 2 0
After:  [0, 0, 0, 1]

Before: [0, 2, 2, 0]
6 0 0 3
After:  [0, 2, 2, 0]

Before: [1, 1, 2, 0]
8 0 2 0
After:  [0, 1, 2, 0]

Before: [2, 3, 2, 0]
9 2 0 2
After:  [2, 3, 1, 0]

Before: [1, 3, 0, 2]
2 0 2 0
After:  [0, 3, 0, 2]

Before: [3, 0, 0, 0]
10 1 0 3
After:  [3, 0, 0, 0]

Before: [0, 1, 0, 1]
6 0 0 0
After:  [0, 1, 0, 1]

Before: [0, 1, 3, 0]
12 3 2 2
After:  [0, 1, 1, 0]

Before: [2, 3, 1, 0]
14 0 3 2
After:  [2, 3, 1, 0]

Before: [0, 1, 2, 1]
11 3 2 1
After:  [0, 1, 2, 1]

Before: [3, 1, 1, 3]
4 2 1 0
After:  [0, 1, 1, 3]

Before: [0, 3, 0, 2]
6 0 0 2
After:  [0, 3, 0, 2]

Before: [0, 3, 2, 1]
11 3 2 3
After:  [0, 3, 2, 1]

Before: [2, 2, 2, 1]
3 1 2 3
After:  [2, 2, 2, 4]

Before: [2, 1, 0, 0]
14 0 3 1
After:  [2, 1, 0, 0]

Before: [0, 3, 3, 3]
9 3 2 2
After:  [0, 3, 1, 3]

Before: [0, 3, 3, 1]
13 0 1 2
After:  [0, 3, 0, 1]

Before: [0, 1, 1, 1]
13 0 3 1
After:  [0, 0, 1, 1]

Before: [2, 0, 2, 1]
3 2 2 2
After:  [2, 0, 4, 1]

Before: [0, 2, 2, 1]
9 2 1 1
After:  [0, 1, 2, 1]

Before: [2, 1, 0, 1]
7 3 3 3
After:  [2, 1, 0, 0]

Before: [0, 0, 1, 3]
13 0 3 0
After:  [0, 0, 1, 3]

Before: [3, 3, 1, 3]
15 2 3 3
After:  [3, 3, 1, 0]

Before: [0, 1, 3, 3]
0 1 2 0
After:  [0, 1, 3, 3]

Before: [3, 0, 3, 0]
12 3 2 0
After:  [1, 0, 3, 0]

Before: [1, 0, 2, 3]
8 0 2 1
After:  [1, 0, 2, 3]

Before: [2, 1, 3, 3]
0 1 2 1
After:  [2, 0, 3, 3]

Before: [2, 0, 3, 3]
4 2 0 1
After:  [2, 1, 3, 3]

Before: [0, 0, 2, 3]
13 0 3 1
After:  [0, 0, 2, 3]

Before: [1, 1, 3, 3]
9 3 2 0
After:  [1, 1, 3, 3]

Before: [0, 0, 0, 1]
6 0 0 2
After:  [0, 0, 0, 1]

Before: [0, 0, 3, 2]
13 0 2 3
After:  [0, 0, 3, 0]

Before: [1, 3, 2, 2]
8 0 2 1
After:  [1, 0, 2, 2]

Before: [0, 1, 0, 1]
13 0 1 2
After:  [0, 1, 0, 1]

Before: [2, 3, 0, 0]
14 0 3 2
After:  [2, 3, 1, 0]

Before: [2, 0, 2, 1]
7 3 3 1
After:  [2, 0, 2, 1]

Before: [3, 3, 2, 2]
7 3 3 2
After:  [3, 3, 0, 2]

Before: [0, 3, 1, 2]
6 0 0 3
After:  [0, 3, 1, 0]

Before: [1, 0, 1, 1]
1 2 0 2
After:  [1, 0, 2, 1]

Before: [2, 1, 1, 0]
14 0 3 1
After:  [2, 1, 1, 0]

Before: [3, 3, 3, 3]
9 3 0 3
After:  [3, 3, 3, 1]

Before: [1, 1, 1, 1]
1 2 3 0
After:  [2, 1, 1, 1]

Before: [3, 1, 3, 1]
0 1 2 2
After:  [3, 1, 0, 1]

Before: [1, 1, 2, 0]
5 1 2 2
After:  [1, 1, 0, 0]

Before: [1, 1, 2, 3]
5 1 2 2
After:  [1, 1, 0, 3]

Before: [2, 0, 0, 3]
10 1 0 1
After:  [2, 0, 0, 3]

Before: [1, 2, 0, 1]
7 3 3 3
After:  [1, 2, 0, 0]

Before: [0, 3, 1, 3]
6 0 0 1
After:  [0, 0, 1, 3]

Before: [2, 2, 3, 1]
4 2 0 3
After:  [2, 2, 3, 1]

Before: [3, 0, 2, 1]
11 3 2 2
After:  [3, 0, 1, 1]

Before: [0, 1, 2, 0]
5 1 2 2
After:  [0, 1, 0, 0]

Before: [2, 3, 1, 1]
1 2 3 2
After:  [2, 3, 2, 1]

Before: [0, 1, 1, 2]
13 0 3 3
After:  [0, 1, 1, 0]

Before: [3, 1, 2, 3]
5 1 2 0
After:  [0, 1, 2, 3]

Before: [1, 3, 3, 0]
12 3 2 0
After:  [1, 3, 3, 0]

Before: [2, 3, 0, 2]
12 2 3 2
After:  [2, 3, 1, 2]

Before: [3, 1, 0, 1]
10 2 0 1
After:  [3, 0, 0, 1]

Before: [0, 2, 0, 0]
13 0 1 0
After:  [0, 2, 0, 0]

Before: [0, 2, 2, 2]
13 0 1 2
After:  [0, 2, 0, 2]

Before: [3, 2, 2, 3]
15 2 3 2
After:  [3, 2, 0, 3]

Before: [2, 0, 2, 0]
14 0 3 1
After:  [2, 1, 2, 0]

Before: [2, 2, 0, 0]
14 0 3 2
After:  [2, 2, 1, 0]

Before: [1, 3, 2, 0]
8 0 2 0
After:  [0, 3, 2, 0]

Before: [3, 2, 3, 1]
9 2 3 1
After:  [3, 0, 3, 1]

Before: [0, 1, 1, 0]
4 2 1 1
After:  [0, 0, 1, 0]

Before: [0, 3, 2, 3]
13 0 3 0
After:  [0, 3, 2, 3]

Before: [3, 1, 0, 1]
7 3 3 3
After:  [3, 1, 0, 0]

Before: [1, 3, 3, 3]
9 3 2 3
After:  [1, 3, 3, 1]

Before: [2, 3, 3, 1]
4 2 0 2
After:  [2, 3, 1, 1]

Before: [0, 3, 3, 1]
7 3 3 0
After:  [0, 3, 3, 1]

Before: [1, 2, 1, 2]
1 2 0 1
After:  [1, 2, 1, 2]

Before: [0, 2, 2, 2]
13 0 2 2
After:  [0, 2, 0, 2]

Before: [1, 1, 3, 3]
0 1 2 1
After:  [1, 0, 3, 3]

Before: [2, 0, 3, 2]
4 0 1 0
After:  [1, 0, 3, 2]

Before: [3, 1, 3, 0]
12 3 2 2
After:  [3, 1, 1, 0]

Before: [0, 2, 1, 1]
1 2 3 3
After:  [0, 2, 1, 2]

Before: [2, 3, 1, 0]
14 0 3 3
After:  [2, 3, 1, 1]

Before: [2, 0, 1, 0]
14 0 3 0
After:  [1, 0, 1, 0]

Before: [0, 3, 1, 1]
7 3 3 3
After:  [0, 3, 1, 0]

Before: [2, 3, 3, 3]
9 3 2 3
After:  [2, 3, 3, 1]

Before: [2, 1, 2, 3]
15 2 3 1
After:  [2, 0, 2, 3]

Before: [2, 1, 3, 3]
0 1 2 2
After:  [2, 1, 0, 3]

Before: [3, 1, 2, 1]
7 3 3 0
After:  [0, 1, 2, 1]

Before: [1, 1, 0, 1]
7 3 3 1
After:  [1, 0, 0, 1]

Before: [2, 1, 2, 1]
5 1 2 2
After:  [2, 1, 0, 1]

Before: [3, 1, 3, 2]
0 1 2 1
After:  [3, 0, 3, 2]

Before: [2, 1, 1, 3]
15 1 3 3
After:  [2, 1, 1, 0]

Before: [3, 2, 0, 1]
10 2 0 3
After:  [3, 2, 0, 0]

Before: [1, 3, 0, 1]
2 0 2 2
After:  [1, 3, 0, 1]

Before: [1, 1, 3, 2]
0 1 2 2
After:  [1, 1, 0, 2]

Before: [1, 2, 2, 2]
7 3 3 0
After:  [0, 2, 2, 2]

Before: [1, 2, 2, 2]
8 0 2 0
After:  [0, 2, 2, 2]

Before: [3, 1, 0, 3]
9 3 0 3
After:  [3, 1, 0, 1]

Before: [1, 1, 0, 1]
2 0 2 2
After:  [1, 1, 0, 1]

Before: [2, 3, 3, 0]
14 0 3 0
After:  [1, 3, 3, 0]

Before: [3, 0, 2, 1]
11 3 2 1
After:  [3, 1, 2, 1]

Before: [2, 3, 3, 0]
14 0 3 3
After:  [2, 3, 3, 1]

Before: [0, 1, 2, 2]
5 1 2 2
After:  [0, 1, 0, 2]

Before: [3, 0, 2, 3]
10 1 0 3
After:  [3, 0, 2, 0]

Before: [1, 1, 2, 3]
8 0 2 2
After:  [1, 1, 0, 3]

Before: [0, 0, 0, 3]
6 0 0 1
After:  [0, 0, 0, 3]

Before: [1, 3, 2, 1]
11 3 2 2
After:  [1, 3, 1, 1]

Before: [0, 3, 1, 3]
13 0 3 1
After:  [0, 0, 1, 3]

Before: [2, 0, 3, 0]
14 0 3 1
After:  [2, 1, 3, 0]

Before: [0, 2, 0, 3]
13 0 3 3
After:  [0, 2, 0, 0]

Before: [1, 0, 2, 0]
8 0 2 2
After:  [1, 0, 0, 0]

Before: [1, 3, 2, 0]
8 0 2 1
After:  [1, 0, 2, 0]

Before: [1, 0, 2, 1]
11 3 2 1
After:  [1, 1, 2, 1]

Before: [1, 0, 0, 0]
2 0 2 1
After:  [1, 0, 0, 0]

Before: [2, 2, 2, 1]
11 3 2 1
After:  [2, 1, 2, 1]

Before: [3, 3, 0, 2]
7 3 3 1
After:  [3, 0, 0, 2]

Before: [2, 1, 3, 3]
15 1 3 0
After:  [0, 1, 3, 3]

Before: [0, 3, 3, 2]
13 0 1 1
After:  [0, 0, 3, 2]

Before: [0, 3, 3, 3]
6 0 0 1
After:  [0, 0, 3, 3]

Before: [1, 3, 2, 2]
8 0 2 2
After:  [1, 3, 0, 2]

Before: [1, 0, 0, 3]
2 0 2 3
After:  [1, 0, 0, 0]

Before: [2, 3, 2, 1]
9 2 0 2
After:  [2, 3, 1, 1]

Before: [1, 3, 1, 2]
1 2 0 0
After:  [2, 3, 1, 2]

Before: [2, 1, 3, 0]
0 1 2 0
After:  [0, 1, 3, 0]

Before: [3, 2, 2, 1]
9 2 1 2
After:  [3, 2, 1, 1]

Before: [2, 1, 3, 1]
0 1 2 2
After:  [2, 1, 0, 1]

Before: [0, 2, 1, 0]
6 0 0 1
After:  [0, 0, 1, 0]

Before: [1, 1, 0, 3]
15 1 3 1
After:  [1, 0, 0, 3]

Before: [0, 3, 3, 3]
9 3 2 3
After:  [0, 3, 3, 1]

Before: [3, 1, 3, 1]
7 3 3 3
After:  [3, 1, 3, 0]

Before: [2, 2, 2, 1]
11 3 2 3
After:  [2, 2, 2, 1]

Before: [3, 2, 2, 3]
9 3 0 1
After:  [3, 1, 2, 3]

Before: [3, 2, 2, 0]
3 1 2 1
After:  [3, 4, 2, 0]

Before: [2, 3, 2, 0]
14 0 3 1
After:  [2, 1, 2, 0]

Before: [0, 1, 3, 0]
0 1 2 2
After:  [0, 1, 0, 0]

Before: [2, 2, 3, 0]
4 2 0 3
After:  [2, 2, 3, 1]

Before: [2, 0, 0, 0]
14 0 3 1
After:  [2, 1, 0, 0]

Before: [1, 1, 0, 0]
2 0 2 0
After:  [0, 1, 0, 0]

Before: [0, 2, 3, 2]
6 0 0 1
After:  [0, 0, 3, 2]

Before: [2, 3, 2, 3]
3 2 2 0
After:  [4, 3, 2, 3]

Before: [1, 2, 2, 1]
3 2 2 0
After:  [4, 2, 2, 1]

Before: [2, 2, 2, 0]
14 0 3 0
After:  [1, 2, 2, 0]

Before: [1, 1, 2, 3]
5 1 2 0
After:  [0, 1, 2, 3]

Before: [3, 1, 3, 3]
9 3 2 0
After:  [1, 1, 3, 3]

Before: [1, 1, 0, 0]
2 0 2 2
After:  [1, 1, 0, 0]

Before: [1, 1, 2, 3]
8 0 2 3
After:  [1, 1, 2, 0]

Before: [3, 3, 2, 3]
3 2 2 1
After:  [3, 4, 2, 3]

Before: [3, 3, 1, 3]
15 2 3 2
After:  [3, 3, 0, 3]

Before: [0, 1, 0, 2]
6 0 0 1
After:  [0, 0, 0, 2]

Before: [1, 1, 3, 0]
12 3 2 0
After:  [1, 1, 3, 0]

Before: [2, 1, 2, 2]
3 3 2 2
After:  [2, 1, 4, 2]

Before: [1, 1, 3, 2]
0 1 2 1
After:  [1, 0, 3, 2]

Before: [3, 1, 2, 3]
5 1 2 1
After:  [3, 0, 2, 3]

Before: [0, 1, 3, 1]
0 1 2 1
After:  [0, 0, 3, 1]

Before: [3, 2, 2, 1]
7 3 3 1
After:  [3, 0, 2, 1]

Before: [0, 1, 2, 3]
5 1 2 2
After:  [0, 1, 0, 3]

Before: [1, 1, 0, 3]
2 0 2 1
After:  [1, 0, 0, 3]

Before: [2, 0, 2, 0]
14 0 3 0
After:  [1, 0, 2, 0]

Before: [0, 2, 1, 0]
6 0 0 2
After:  [0, 2, 0, 0]

Before: [0, 2, 0, 1]
13 0 1 0
After:  [0, 2, 0, 1]

Before: [2, 3, 0, 0]
14 0 3 0
After:  [1, 3, 0, 0]

Before: [3, 1, 1, 3]
15 1 3 3
After:  [3, 1, 1, 0]

Before: [1, 2, 1, 3]
15 2 3 3
After:  [1, 2, 1, 0]

Before: [3, 1, 2, 1]
5 1 2 1
After:  [3, 0, 2, 1]

Before: [1, 1, 0, 1]
2 0 2 1
After:  [1, 0, 0, 1]

Before: [1, 2, 2, 3]
8 0 2 0
After:  [0, 2, 2, 3]

Before: [0, 2, 2, 3]
15 2 3 2
After:  [0, 2, 0, 3]

Before: [1, 0, 2, 0]
8 0 2 0
After:  [0, 0, 2, 0]

Before: [0, 2, 2, 3]
3 2 2 0
After:  [4, 2, 2, 3]

Before: [3, 3, 2, 1]
11 3 2 2
After:  [3, 3, 1, 1]

Before: [0, 2, 2, 2]
6 0 0 2
After:  [0, 2, 0, 2]

Before: [1, 1, 2, 1]
5 1 2 3
After:  [1, 1, 2, 0]

Before: [2, 0, 2, 1]
11 3 2 1
After:  [2, 1, 2, 1]

Before: [0, 1, 2, 1]
5 1 2 3
After:  [0, 1, 2, 0]

Before: [1, 2, 2, 2]
3 1 2 0
After:  [4, 2, 2, 2]

Before: [1, 3, 2, 1]
11 3 2 3
After:  [1, 3, 2, 1]

Before: [0, 1, 1, 2]
13 0 1 2
After:  [0, 1, 0, 2]

Before: [1, 2, 2, 0]
3 1 2 1
After:  [1, 4, 2, 0]

Before: [1, 0, 0, 0]
2 0 2 0
After:  [0, 0, 0, 0]

Before: [1, 2, 1, 1]
1 2 0 3
After:  [1, 2, 1, 2]

Before: [3, 3, 2, 1]
11 3 2 1
After:  [3, 1, 2, 1]

Before: [0, 0, 2, 1]
11 3 2 0
After:  [1, 0, 2, 1]

Before: [1, 1, 1, 3]
4 2 1 3
After:  [1, 1, 1, 0]

Before: [2, 0, 2, 2]
7 3 3 1
After:  [2, 0, 2, 2]

Before: [0, 1, 2, 1]
5 1 2 0
After:  [0, 1, 2, 1]

Before: [3, 2, 0, 3]
10 2 0 0
After:  [0, 2, 0, 3]

Before: [1, 1, 2, 0]
5 1 2 1
After:  [1, 0, 2, 0]

Before: [2, 0, 3, 1]
9 2 3 2
After:  [2, 0, 0, 1]

Before: [1, 0, 2, 1]
8 0 2 1
After:  [1, 0, 2, 1]

Before: [0, 2, 0, 3]
15 1 3 3
After:  [0, 2, 0, 0]

Before: [0, 2, 2, 0]
6 0 0 0
After:  [0, 2, 2, 0]

Before: [0, 0, 1, 1]
1 2 3 2
After:  [0, 0, 2, 1]

Before: [1, 0, 1, 3]
15 2 3 3
After:  [1, 0, 1, 0]

Before: [2, 1, 2, 3]
15 1 3 2
After:  [2, 1, 0, 3]

Before: [1, 2, 2, 3]
8 0 2 2
After:  [1, 2, 0, 3]

Before: [2, 2, 3, 0]
12 3 2 2
After:  [2, 2, 1, 0]

Before: [3, 1, 3, 1]
9 2 3 3
After:  [3, 1, 3, 0]

Before: [3, 0, 3, 1]
7 3 3 1
After:  [3, 0, 3, 1]

Before: [0, 3, 0, 2]
6 0 0 3
After:  [0, 3, 0, 0]

Before: [1, 1, 2, 1]
5 1 2 0
After:  [0, 1, 2, 1]

Before: [1, 3, 3, 0]
12 3 2 3
After:  [1, 3, 3, 1]

Before: [3, 0, 1, 1]
1 2 3 0
After:  [2, 0, 1, 1]

Before: [2, 1, 2, 0]
14 0 3 3
After:  [2, 1, 2, 1]

Before: [2, 3, 2, 1]
11 3 2 2
After:  [2, 3, 1, 1]

Before: [0, 3, 3, 0]
6 0 0 3
After:  [0, 3, 3, 0]

Before: [0, 1, 3, 0]
12 3 2 3
After:  [0, 1, 3, 1]

Before: [1, 2, 3, 0]
12 3 2 3
After:  [1, 2, 3, 1]

Before: [2, 1, 0, 2]
12 2 3 3
After:  [2, 1, 0, 1]

Before: [0, 3, 0, 2]
7 3 3 3
After:  [0, 3, 0, 0]

Before: [3, 0, 3, 0]
12 3 2 2
After:  [3, 0, 1, 0]

Before: [2, 2, 0, 0]
14 0 3 3
After:  [2, 2, 0, 1]

Before: [1, 2, 0, 1]
2 0 2 1
After:  [1, 0, 0, 1]

Before: [0, 2, 3, 1]
9 2 3 2
After:  [0, 2, 0, 1]

Before: [2, 1, 2, 1]
11 3 2 1
After:  [2, 1, 2, 1]

Before: [3, 1, 3, 3]
0 1 2 3
After:  [3, 1, 3, 0]

Before: [0, 1, 2, 3]
5 1 2 3
After:  [0, 1, 2, 0]

Before: [1, 3, 1, 0]
1 2 0 2
After:  [1, 3, 2, 0]

Before: [0, 3, 3, 2]
13 0 1 3
After:  [0, 3, 3, 0]

Before: [1, 2, 0, 2]
2 0 2 0
After:  [0, 2, 0, 2]

Before: [2, 2, 0, 0]
14 0 3 0
After:  [1, 2, 0, 0]

Before: [3, 2, 0, 0]
10 2 0 0
After:  [0, 2, 0, 0]

Before: [1, 2, 2, 0]
8 0 2 0
After:  [0, 2, 2, 0]

Before: [2, 0, 2, 2]
3 3 2 1
After:  [2, 4, 2, 2]

Before: [1, 3, 0, 2]
12 2 3 1
After:  [1, 1, 0, 2]

Before: [0, 1, 1, 2]
7 3 3 3
After:  [0, 1, 1, 0]

Before: [0, 0, 1, 2]
7 3 3 1
After:  [0, 0, 1, 2]

Before: [0, 1, 1, 0]
6 0 0 1
After:  [0, 0, 1, 0]

Before: [2, 0, 2, 1]
11 3 2 0
After:  [1, 0, 2, 1]

Before: [2, 2, 3, 3]
15 1 3 1
After:  [2, 0, 3, 3]

Before: [0, 3, 2, 3]
13 0 2 3
After:  [0, 3, 2, 0]

Before: [0, 1, 2, 2]
13 0 3 3
After:  [0, 1, 2, 0]

Before: [2, 1, 2, 0]
5 1 2 0
After:  [0, 1, 2, 0]

Before: [3, 3, 0, 2]
7 3 3 3
After:  [3, 3, 0, 0]

Before: [0, 0, 1, 2]
13 0 3 2
After:  [0, 0, 0, 2]

Before: [1, 3, 1, 2]
1 2 0 3
After:  [1, 3, 1, 2]

Before: [0, 1, 3, 1]
13 0 3 1
After:  [0, 0, 3, 1]

Before: [2, 1, 3, 1]
4 2 0 0
After:  [1, 1, 3, 1]

Before: [1, 1, 2, 2]
8 0 2 2
After:  [1, 1, 0, 2]

Before: [3, 0, 0, 2]
10 1 0 3
After:  [3, 0, 0, 0]

Before: [0, 3, 1, 2]
7 3 3 2
After:  [0, 3, 0, 2]

Before: [3, 2, 2, 2]
9 2 1 2
After:  [3, 2, 1, 2]

Before: [0, 3, 2, 2]
4 3 2 1
After:  [0, 0, 2, 2]

Before: [0, 1, 2, 3]
5 1 2 0
After:  [0, 1, 2, 3]

Before: [1, 2, 0, 3]
2 0 2 3
After:  [1, 2, 0, 0]

Before: [0, 3, 2, 3]
13 0 2 0
After:  [0, 3, 2, 3]

Before: [1, 1, 2, 0]
8 0 2 2
After:  [1, 1, 0, 0]

Before: [1, 2, 0, 0]
2 0 2 2
After:  [1, 2, 0, 0]

Before: [0, 0, 2, 1]
11 3 2 2
After:  [0, 0, 1, 1]

Before: [3, 1, 3, 2]
0 1 2 2
After:  [3, 1, 0, 2]

Before: [1, 1, 1, 1]
4 3 1 1
After:  [1, 0, 1, 1]

Before: [0, 3, 3, 1]
13 0 3 1
After:  [0, 0, 3, 1]

Before: [1, 1, 3, 0]
12 3 2 1
After:  [1, 1, 3, 0]

Before: [2, 0, 0, 0]
14 0 3 0
After:  [1, 0, 0, 0]

Before: [0, 1, 3, 2]
0 1 2 3
After:  [0, 1, 3, 0]

Before: [1, 1, 2, 0]
8 0 2 3
After:  [1, 1, 2, 0]

Before: [3, 0, 2, 3]
15 2 3 2
After:  [3, 0, 0, 3]

Before: [1, 1, 1, 2]
1 2 0 0
After:  [2, 1, 1, 2]

Before: [3, 3, 2, 2]
3 2 2 2
After:  [3, 3, 4, 2]

Before: [0, 1, 0, 2]
7 3 3 2
After:  [0, 1, 0, 2]

Before: [0, 2, 2, 2]
13 0 2 0
After:  [0, 2, 2, 2]

Before: [3, 1, 0, 0]
10 2 0 3
After:  [3, 1, 0, 0]

Before: [2, 1, 3, 0]
0 1 2 1
After:  [2, 0, 3, 0]

Before: [1, 0, 2, 2]
8 0 2 1
After:  [1, 0, 2, 2]

Before: [2, 0, 1, 2]
10 1 0 1
After:  [2, 0, 1, 2]

Before: [2, 3, 2, 1]
11 3 2 1
After:  [2, 1, 2, 1]

Before: [2, 1, 1, 1]
4 2 1 3
After:  [2, 1, 1, 0]

Before: [2, 0, 2, 1]
11 3 2 2
After:  [2, 0, 1, 1]

Before: [2, 1, 3, 2]
0 1 2 1
After:  [2, 0, 3, 2]

Before: [2, 1, 2, 0]
5 1 2 3
After:  [2, 1, 2, 0]

Before: [0, 3, 2, 3]
13 0 1 3
After:  [0, 3, 2, 0]

Before: [1, 1, 2, 2]
5 1 2 0
After:  [0, 1, 2, 2]

Before: [1, 3, 1, 1]
1 2 3 3
After:  [1, 3, 1, 2]

Before: [2, 0, 2, 0]
14 0 3 2
After:  [2, 0, 1, 0]

Before: [3, 2, 2, 1]
11 3 2 1
After:  [3, 1, 2, 1]

Before: [1, 1, 3, 2]
0 1 2 0
After:  [0, 1, 3, 2]

Before: [0, 2, 2, 1]
11 3 2 1
After:  [0, 1, 2, 1]

Before: [2, 0, 0, 3]
10 1 0 3
After:  [2, 0, 0, 0]

Before: [2, 1, 0, 3]
15 1 3 1
After:  [2, 0, 0, 3]

Before: [3, 0, 2, 2]
4 3 2 1
After:  [3, 0, 2, 2]

Before: [3, 2, 2, 1]
11 3 2 2
After:  [3, 2, 1, 1]

Before: [2, 0, 0, 2]
12 2 3 2
After:  [2, 0, 1, 2]

Before: [0, 1, 2, 2]
6 0 0 0
After:  [0, 1, 2, 2]

Before: [2, 2, 2, 3]
3 2 2 1
After:  [2, 4, 2, 3]

Before: [2, 1, 2, 3]
5 1 2 3
After:  [2, 1, 2, 0]

Before: [0, 3, 3, 2]
6 0 0 0
After:  [0, 3, 3, 2]

Before: [3, 0, 3, 1]
7 3 3 0
After:  [0, 0, 3, 1]

Before: [0, 1, 1, 3]
15 1 3 1
After:  [0, 0, 1, 3]

Before: [0, 1, 3, 3]
15 1 3 3
After:  [0, 1, 3, 0]

Before: [2, 3, 2, 2]
4 3 2 0
After:  [0, 3, 2, 2]

Before: [0, 0, 2, 2]
7 3 3 2
After:  [0, 0, 0, 2]

Before: [2, 1, 1, 2]
4 2 1 1
After:  [2, 0, 1, 2]

Before: [1, 2, 0, 3]
2 0 2 0
After:  [0, 2, 0, 3]

Before: [3, 1, 2, 3]
9 3 0 3
After:  [3, 1, 2, 1]

Before: [0, 0, 0, 3]
13 0 3 0
After:  [0, 0, 0, 3]

Before: [1, 2, 2, 1]
8 0 2 2
After:  [1, 2, 0, 1]

Before: [3, 0, 1, 3]
9 3 0 3
After:  [3, 0, 1, 1]

Before: [1, 1, 2, 2]
5 1 2 1
After:  [1, 0, 2, 2]

Before: [1, 0, 2, 1]
11 3 2 0
After:  [1, 0, 2, 1]

Before: [0, 2, 3, 0]
12 3 2 3
After:  [0, 2, 3, 1]

Before: [3, 1, 3, 3]
0 1 2 1
After:  [3, 0, 3, 3]

Before: [3, 1, 0, 2]
7 3 3 0
After:  [0, 1, 0, 2]

Before: [1, 2, 0, 1]
2 0 2 3
After:  [1, 2, 0, 0]

Before: [1, 0, 2, 1]
8 0 2 3
After:  [1, 0, 2, 0]

Before: [2, 0, 2, 0]
10 1 0 1
After:  [2, 0, 2, 0]

Before: [3, 0, 3, 1]
10 1 0 2
After:  [3, 0, 0, 1]

Before: [3, 0, 3, 3]
9 3 0 1
After:  [3, 1, 3, 3]

Before: [0, 1, 3, 1]
13 0 2 1
After:  [0, 0, 3, 1]

Before: [0, 1, 1, 0]
6 0 0 3
After:  [0, 1, 1, 0]

Before: [0, 3, 3, 1]
13 0 3 3
After:  [0, 3, 3, 0]

Before: [1, 3, 0, 3]
2 0 2 0
After:  [0, 3, 0, 3]

Before: [2, 3, 3, 0]
12 3 2 2
After:  [2, 3, 1, 0]

Before: [3, 2, 1, 3]
15 1 3 0
After:  [0, 2, 1, 3]

Before: [1, 3, 2, 1]
8 0 2 2
After:  [1, 3, 0, 1]

Before: [3, 0, 3, 2]
10 1 0 1
After:  [3, 0, 3, 2]

Before: [3, 0, 2, 0]
10 1 0 2
After:  [3, 0, 0, 0]

Before: [2, 2, 3, 0]
14 0 3 1
After:  [2, 1, 3, 0]

Before: [3, 1, 2, 2]
5 1 2 1
After:  [3, 0, 2, 2]

Before: [1, 1, 2, 1]
5 1 2 1
After:  [1, 0, 2, 1]

Before: [1, 2, 2, 1]
11 3 2 2
After:  [1, 2, 1, 1]

Before: [3, 3, 2, 1]
11 3 2 0
After:  [1, 3, 2, 1]

Before: [0, 2, 0, 1]
6 0 0 3
After:  [0, 2, 0, 0]

Before: [2, 1, 2, 1]
11 3 2 2
After:  [2, 1, 1, 1]

Before: [1, 1, 3, 0]
0 1 2 1
After:  [1, 0, 3, 0]

Before: [3, 1, 2, 0]
5 1 2 2
After:  [3, 1, 0, 0]

Before: [0, 1, 2, 1]
5 1 2 2
After:  [0, 1, 0, 1]

Before: [0, 2, 3, 1]
13 0 1 1
After:  [0, 0, 3, 1]

Before: [1, 2, 3, 0]
12 3 2 1
After:  [1, 1, 3, 0]

Before: [1, 0, 3, 0]
12 3 2 0
After:  [1, 0, 3, 0]

Before: [2, 3, 0, 0]
14 0 3 1
After:  [2, 1, 0, 0]

Before: [0, 3, 1, 1]
7 3 3 1
After:  [0, 0, 1, 1]

Before: [3, 1, 3, 2]
0 1 2 3
After:  [3, 1, 3, 0]

Before: [0, 1, 3, 1]
9 2 3 1
After:  [0, 0, 3, 1]

Before: [3, 3, 0, 2]
12 2 3 3
After:  [3, 3, 0, 1]

Before: [1, 3, 2, 1]
11 3 2 0
After:  [1, 3, 2, 1]

Before: [0, 3, 1, 1]
7 3 3 0
After:  [0, 3, 1, 1]

Before: [1, 3, 3, 1]
7 3 3 3
After:  [1, 3, 3, 0]

Before: [2, 1, 2, 2]
5 1 2 3
After:  [2, 1, 2, 0]

Before: [2, 1, 3, 1]
9 2 3 1
After:  [2, 0, 3, 1]

Before: [0, 2, 2, 1]
13 0 1 0
After:  [0, 2, 2, 1]

Before: [0, 1, 2, 1]
11 3 2 0
After:  [1, 1, 2, 1]

Before: [0, 1, 3, 3]
0 1 2 3
After:  [0, 1, 3, 0]

Before: [1, 1, 3, 3]
0 1 2 0
After:  [0, 1, 3, 3]

Before: [1, 0, 1, 2]
1 2 0 1
After:  [1, 2, 1, 2]

Before: [1, 0, 1, 3]
1 2 0 2
After:  [1, 0, 2, 3]

Before: [2, 1, 2, 0]
3 0 2 3
After:  [2, 1, 2, 4]

Before: [3, 0, 2, 2]
7 3 3 0
After:  [0, 0, 2, 2]

Before: [3, 0, 0, 2]
10 1 0 0
After:  [0, 0, 0, 2]

Before: [2, 1, 3, 2]
7 3 3 3
After:  [2, 1, 3, 0]

Before: [2, 0, 2, 1]
4 0 1 1
After:  [2, 1, 2, 1]

Before: [3, 3, 3, 0]
12 3 2 1
After:  [3, 1, 3, 0]

Before: [1, 0, 2, 3]
8 0 2 0
After:  [0, 0, 2, 3]

Before: [0, 1, 1, 3]
15 1 3 0
After:  [0, 1, 1, 3]

Before: [2, 0, 3, 3]
9 3 2 2
After:  [2, 0, 1, 3]

Before: [2, 3, 0, 0]
14 0 3 3
After:  [2, 3, 0, 1]

Before: [2, 3, 2, 1]
11 3 2 3
After:  [2, 3, 2, 1]

Before: [2, 0, 0, 3]
4 0 1 2
After:  [2, 0, 1, 3]

Before: [0, 1, 1, 2]
6 0 0 0
After:  [0, 1, 1, 2]

Before: [1, 0, 3, 0]
12 3 2 1
After:  [1, 1, 3, 0]

Before: [2, 1, 1, 1]
1 2 3 2
After:  [2, 1, 2, 1]

Before: [1, 3, 2, 2]
3 2 2 3
After:  [1, 3, 2, 4]

Before: [0, 1, 1, 1]
1 2 3 1
After:  [0, 2, 1, 1]

Before: [2, 1, 3, 2]
0 1 2 0
After:  [0, 1, 3, 2]

Before: [1, 0, 2, 0]
8 0 2 3
After:  [1, 0, 2, 0]

Before: [0, 3, 2, 3]
3 2 2 2
After:  [0, 3, 4, 3]

Before: [1, 2, 1, 1]
1 2 3 3
After:  [1, 2, 1, 2]

Before: [2, 3, 2, 1]
3 2 2 3
After:  [2, 3, 2, 4]

Before: [3, 1, 1, 1]
1 2 3 2
After:  [3, 1, 2, 1]

Before: [2, 3, 2, 0]
9 2 0 1
After:  [2, 1, 2, 0]

Before: [2, 0, 2, 1]
11 3 2 3
After:  [2, 0, 2, 1]

Before: [1, 1, 2, 0]
3 2 2 2
After:  [1, 1, 4, 0]

Before: [2, 2, 2, 1]
11 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 0, 0, 2]
2 0 2 0
After:  [0, 0, 0, 2]

Before: [1, 0, 3, 0]
12 3 2 3
After:  [1, 0, 3, 1]

Before: [3, 1, 0, 3]
4 0 2 3
After:  [3, 1, 0, 1]

Before: [3, 2, 2, 1]
3 2 2 0
After:  [4, 2, 2, 1]

Before: [3, 1, 2, 3]
5 1 2 3
After:  [3, 1, 2, 0]

Before: [3, 1, 2, 2]
3 2 2 2
After:  [3, 1, 4, 2]

Before: [3, 0, 1, 1]
7 3 3 0
After:  [0, 0, 1, 1]

Before: [1, 0, 3, 0]
12 3 2 2
After:  [1, 0, 1, 0]

Before: [2, 3, 3, 0]
4 2 0 0
After:  [1, 3, 3, 0]

Before: [2, 2, 1, 0]
14 0 3 3
After:  [2, 2, 1, 1]

Before: [1, 2, 0, 3]
2 0 2 1
After:  [1, 0, 0, 3]

Before: [0, 2, 2, 1]
9 2 1 0
After:  [1, 2, 2, 1]

Before: [3, 1, 3, 1]
0 1 2 0
After:  [0, 1, 3, 1]

Before: [0, 1, 2, 3]
6 0 0 0
After:  [0, 1, 2, 3]

Before: [3, 0, 1, 2]
10 1 0 1
After:  [3, 0, 1, 2]

Before: [2, 2, 2, 1]
7 3 3 3
After:  [2, 2, 2, 0]

Before: [3, 0, 1, 3]
10 1 0 0
After:  [0, 0, 1, 3]

Before: [0, 0, 3, 0]
12 3 2 3
After:  [0, 0, 3, 1]

Before: [2, 1, 2, 0]
5 1 2 1
After:  [2, 0, 2, 0]

Before: [2, 2, 2, 3]
15 2 3 2
After:  [2, 2, 0, 3]

Before: [2, 0, 3, 0]
14 0 3 3
After:  [2, 0, 3, 1]

Before: [1, 1, 3, 3]
0 1 2 2
After:  [1, 1, 0, 3]

Before: [0, 1, 1, 2]
6 0 0 3
After:  [0, 1, 1, 0]

Before: [2, 2, 2, 3]
15 1 3 3
After:  [2, 2, 2, 0]

Before: [2, 3, 2, 0]
14 0 3 3
After:  [2, 3, 2, 1]

Before: [0, 1, 3, 3]
0 1 2 1
After:  [0, 0, 3, 3]

Before: [1, 3, 2, 2]
4 3 2 0
After:  [0, 3, 2, 2]

Before: [2, 1, 1, 3]
4 2 1 3
After:  [2, 1, 1, 0]

Before: [2, 1, 0, 0]
14 0 3 3
After:  [2, 1, 0, 1]

Before: [0, 2, 1, 3]
15 1 3 1
After:  [0, 0, 1, 3]

Before: [2, 1, 3, 0]
0 1 2 2
After:  [2, 1, 0, 0]

Before: [1, 2, 0, 2]
12 2 3 0
After:  [1, 2, 0, 2]

Before: [0, 3, 0, 3]
13 0 3 3
After:  [0, 3, 0, 0]

Before: [3, 3, 0, 1]
10 2 0 1
After:  [3, 0, 0, 1]

Before: [2, 1, 1, 0]
14 0 3 3
After:  [2, 1, 1, 1]

Before: [1, 2, 2, 0]
8 0 2 2
After:  [1, 2, 0, 0]

Before: [2, 0, 0, 3]
4 0 1 0
After:  [1, 0, 0, 3]

Before: [1, 1, 2, 1]
5 1 2 2
After:  [1, 1, 0, 1]

Before: [3, 0, 3, 3]
9 3 2 0
After:  [1, 0, 3, 3]

Before: [1, 2, 2, 3]
9 2 1 0
After:  [1, 2, 2, 3]

Before: [2, 3, 2, 0]
14 0 3 0
After:  [1, 3, 2, 0]

Before: [3, 2, 3, 1]
7 3 3 3
After:  [3, 2, 3, 0]

Before: [0, 1, 3, 0]
0 1 2 1
After:  [0, 0, 3, 0]

Before: [3, 3, 0, 3]
9 3 0 2
After:  [3, 3, 1, 3]

Before: [3, 1, 3, 2]
0 1 2 0
After:  [0, 1, 3, 2]

Before: [0, 0, 2, 1]
11 3 2 3
After:  [0, 0, 2, 1]

Before: [0, 2, 1, 3]
13 0 1 3
After:  [0, 2, 1, 0]

Before: [1, 2, 2, 2]
3 1 2 3
After:  [1, 2, 2, 4]

Before: [0, 1, 2, 3]
5 1 2 1
After:  [0, 0, 2, 3]

Before: [2, 0, 3, 2]
10 1 0 0
After:  [0, 0, 3, 2]

Before: [1, 1, 0, 2]
12 2 3 0
After:  [1, 1, 0, 2]

Before: [3, 3, 1, 1]
1 2 3 0
After:  [2, 3, 1, 1]

Before: [1, 1, 0, 3]
2 0 2 3
After:  [1, 1, 0, 0]

Before: [1, 3, 1, 1]
1 2 0 2
After:  [1, 3, 2, 1]

Before: [2, 1, 2, 0]
14 0 3 1
After:  [2, 1, 2, 0]

Before: [2, 0, 2, 1]
4 0 1 3
After:  [2, 0, 2, 1]

Before: [2, 0, 2, 0]
14 0 3 3
After:  [2, 0, 2, 1]

Before: [0, 1, 3, 1]
0 1 2 2
After:  [0, 1, 0, 1]

Before: [1, 1, 2, 2]
3 2 2 1
After:  [1, 4, 2, 2]

Before: [0, 2, 3, 1]
6 0 0 3
After:  [0, 2, 3, 0]

Before: [1, 3, 0, 2]
2 0 2 3
After:  [1, 3, 0, 0]

Before: [1, 0, 1, 1]
1 2 3 3
After:  [1, 0, 1, 2]

Before: [1, 3, 1, 1]
1 2 3 0
After:  [2, 3, 1, 1]

Before: [1, 2, 2, 2]
9 2 1 0
After:  [1, 2, 2, 2]

Before: [2, 1, 3, 0]
14 0 3 1
After:  [2, 1, 3, 0]

Before: [1, 2, 1, 3]
1 2 0 0
After:  [2, 2, 1, 3]

Before: [1, 0, 0, 0]
2 0 2 2
After:  [1, 0, 0, 0]

Before: [2, 0, 2, 2]
3 2 2 0
After:  [4, 0, 2, 2]

Before: [2, 0, 3, 2]
4 0 1 3
After:  [2, 0, 3, 1]

Before: [2, 1, 2, 1]
5 1 2 3
After:  [2, 1, 2, 0]

Before: [1, 2, 2, 3]
15 2 3 1
After:  [1, 0, 2, 3]

Before: [0, 3, 2, 1]
6 0 0 2
After:  [0, 3, 0, 1]

Before: [1, 0, 0, 3]
2 0 2 2
After:  [1, 0, 0, 3]

Before: [1, 3, 2, 2]
8 0 2 0
After:  [0, 3, 2, 2]

Before: [0, 2, 1, 1]
6 0 0 1
After:  [0, 0, 1, 1]

Before: [2, 0, 2, 3]
9 2 0 1
After:  [2, 1, 2, 3]

Before: [2, 1, 2, 0]
14 0 3 2
After:  [2, 1, 1, 0]

Before: [1, 0, 1, 2]
1 2 0 3
After:  [1, 0, 1, 2]

Before: [2, 2, 3, 0]
12 3 2 3
After:  [2, 2, 3, 1]

Before: [3, 3, 3, 3]
9 3 2 1
After:  [3, 1, 3, 3]

Before: [0, 2, 2, 2]
3 1 2 3
After:  [0, 2, 2, 4]

Before: [2, 2, 2, 1]
9 2 1 1
After:  [2, 1, 2, 1]

Before: [1, 3, 0, 0]
2 0 2 1
After:  [1, 0, 0, 0]

Before: [2, 1, 2, 0]
14 0 3 0
After:  [1, 1, 2, 0]

Before: [1, 3, 0, 1]
2 0 2 3
After:  [1, 3, 0, 0]

Before: [1, 3, 1, 1]
1 2 3 1
After:  [1, 2, 1, 1]

Before: [1, 3, 0, 3]
2 0 2 1
After:  [1, 0, 0, 3]

Before: [3, 1, 2, 3]
15 2 3 2
After:  [3, 1, 0, 3]

Before: [2, 3, 3, 3]
9 3 2 0
After:  [1, 3, 3, 3]

Before: [0, 1, 3, 1]
0 1 2 3
After:  [0, 1, 3, 0]

Before: [1, 0, 1, 1]
1 2 0 1
After:  [1, 2, 1, 1]

Before: [1, 0, 2, 1]
8 0 2 0
After:  [0, 0, 2, 1]

Before: [1, 2, 2, 2]
8 0 2 1
After:  [1, 0, 2, 2]

Before: [3, 2, 1, 3]
9 3 0 0
After:  [1, 2, 1, 3]

Before: [2, 1, 3, 2]
0 1 2 3
After:  [2, 1, 3, 0]

Before: [2, 2, 2, 0]
3 2 2 0
After:  [4, 2, 2, 0]

Before: [3, 3, 2, 3]
15 2 3 1
After:  [3, 0, 2, 3]

Before: [3, 0, 1, 1]
10 1 0 3
After:  [3, 0, 1, 0]

Before: [0, 1, 3, 3]
6 0 0 1
After:  [0, 0, 3, 3]

Before: [0, 0, 3, 3]
9 3 2 0
After:  [1, 0, 3, 3]

Before: [0, 2, 1, 1]
1 2 3 0
After:  [2, 2, 1, 1]

Before: [2, 3, 1, 0]
14 0 3 1
After:  [2, 1, 1, 0]

Before: [3, 0, 0, 3]
9 3 0 1
After:  [3, 1, 0, 3]

Before: [0, 0, 0, 2]
6 0 0 0
After:  [0, 0, 0, 2]

Before: [1, 3, 2, 0]
8 0 2 3
After:  [1, 3, 2, 0]

Before: [0, 3, 1, 1]
13 0 3 1
After:  [0, 0, 1, 1]

Before: [1, 2, 1, 1]
1 2 3 0
After:  [2, 2, 1, 1]

Before: [0, 1, 1, 2]
13 0 1 3
After:  [0, 1, 1, 0]

Before: [1, 2, 0, 0]
2 0 2 0
After:  [0, 2, 0, 0]

Before: [0, 0, 0, 0]
6 0 0 1
After:  [0, 0, 0, 0]

Before: [0, 0, 3, 0]
12 3 2 0
After:  [1, 0, 3, 0]

Before: [0, 3, 2, 2]
4 3 2 3
After:  [0, 3, 2, 0]

Before: [3, 3, 3, 2]
7 3 3 2
After:  [3, 3, 0, 2]

Before: [0, 2, 0, 1]
13 0 3 1
After:  [0, 0, 0, 1]

Before: [3, 1, 3, 1]
0 1 2 3
After:  [3, 1, 3, 0]

Before: [3, 1, 2, 0]
5 1 2 1
After:  [3, 0, 2, 0]

Before: [0, 1, 2, 0]
5 1 2 0
After:  [0, 1, 2, 0]

Before: [0, 1, 3, 3]
0 1 2 2
After:  [0, 1, 0, 3]

Before: [1, 0, 0, 2]
2 0 2 1
After:  [1, 0, 0, 2]

Before: [2, 3, 1, 3]
15 2 3 2
After:  [2, 3, 0, 3]

Before: [2, 2, 1, 2]
7 3 3 1
After:  [2, 0, 1, 2]

Before: [0, 1, 0, 2]
7 3 3 3
After:  [0, 1, 0, 0]

Before: [1, 1, 2, 2]
3 3 2 2
After:  [1, 1, 4, 2]

Before: [2, 0, 1, 1]
1 2 3 1
After:  [2, 2, 1, 1]

Before: [1, 2, 0, 1]
2 0 2 2
After:  [1, 2, 0, 1]

Before: [0, 1, 1, 0]
6 0 0 2
After:  [0, 1, 0, 0]

Before: [2, 0, 2, 3]
3 0 2 1
After:  [2, 4, 2, 3]

Before: [0, 1, 2, 0]
5 1 2 1
After:  [0, 0, 2, 0]

Before: [2, 2, 2, 3]
3 0 2 0
After:  [4, 2, 2, 3]

Before: [1, 1, 2, 3]
15 2 3 0
After:  [0, 1, 2, 3]

Before: [0, 1, 2, 1]
3 2 2 2
After:  [0, 1, 4, 1]

Before: [2, 1, 2, 3]
5 1 2 2
After:  [2, 1, 0, 3]

Before: [3, 3, 0, 2]
12 2 3 0
After:  [1, 3, 0, 2]

Before: [3, 1, 3, 1]
0 1 2 1
After:  [3, 0, 3, 1]

Before: [3, 0, 3, 0]
12 3 2 1
After:  [3, 1, 3, 0]

Before: [2, 2, 2, 0]
14 0 3 1
After:  [2, 1, 2, 0]

Before: [1, 1, 0, 1]
2 0 2 0
After:  [0, 1, 0, 1]

Before: [3, 3, 1, 1]
1 2 3 3
After:  [3, 3, 1, 2]

Before: [0, 3, 0, 2]
12 2 3 1
After:  [0, 1, 0, 2]

Before: [1, 1, 2, 2]
3 2 2 0
After:  [4, 1, 2, 2]

Before: [3, 2, 2, 1]
11 3 2 3
After:  [3, 2, 2, 1]

Before: [0, 1, 2, 1]
13 0 1 3
After:  [0, 1, 2, 0]

Before: [1, 1, 1, 2]
1 2 0 1
After:  [1, 2, 1, 2]

Before: [0, 3, 2, 1]
11 3 2 2
After:  [0, 3, 1, 1]

Before: [1, 1, 3, 3]
0 1 2 3
After:  [1, 1, 3, 0]

Before: [3, 1, 0, 2]
4 0 2 0
After:  [1, 1, 0, 2]

Before: [1, 1, 3, 0]
0 1 2 2
After:  [1, 1, 0, 0]

Before: [1, 2, 0, 2]
2 0 2 1
After:  [1, 0, 0, 2]

Before: [1, 0, 1, 2]
1 2 0 0
After:  [2, 0, 1, 2]

Before: [3, 1, 2, 1]
5 1 2 0
After:  [0, 1, 2, 1]

Before: [2, 2, 2, 1]
11 3 2 2
After:  [2, 2, 1, 1]

Before: [0, 1, 2, 0]
5 1 2 3
After:  [0, 1, 2, 0]

Before: [3, 3, 1, 2]
7 3 3 1
After:  [3, 0, 1, 2]

Before: [3, 1, 2, 2]
5 1 2 2
After:  [3, 1, 0, 2]

Before: [1, 3, 0, 3]
2 0 2 3
After:  [1, 3, 0, 0]

Before: [1, 1, 2, 0]
5 1 2 0
After:  [0, 1, 2, 0]

Before: [1, 1, 2, 2]
3 3 2 1
After:  [1, 4, 2, 2]

Before: [3, 0, 2, 1]
10 1 0 0
After:  [0, 0, 2, 1]

Before: [0, 0, 1, 1]
1 2 3 1
After:  [0, 2, 1, 1]

Before: [0, 3, 2, 1]
11 3 2 0
After:  [1, 3, 2, 1]

Before: [3, 3, 0, 3]
10 2 0 1
After:  [3, 0, 0, 3]

Before: [2, 2, 3, 1]
9 2 3 2
After:  [2, 2, 0, 1]

Before: [1, 1, 2, 1]
8 0 2 2
After:  [1, 1, 0, 1]

Before: [2, 1, 2, 1]
5 1 2 0
After:  [0, 1, 2, 1]

Before: [3, 1, 3, 0]
12 3 2 0
After:  [1, 1, 3, 0]

Before: [1, 0, 0, 2]
12 2 3 2
After:  [1, 0, 1, 2]

Before: [1, 3, 2, 1]
8 0 2 0
After:  [0, 3, 2, 1]

Before: [3, 2, 2, 3]
3 1 2 2
After:  [3, 2, 4, 3]

Before: [0, 2, 2, 2]
4 3 2 3
After:  [0, 2, 2, 0]

Before: [3, 1, 2, 1]
5 1 2 3
After:  [3, 1, 2, 0]

Before: [0, 2, 0, 2]
6 0 0 2
After:  [0, 2, 0, 2]

Before: [3, 1, 0, 3]
15 1 3 1
After:  [3, 0, 0, 3]

Before: [2, 2, 2, 0]
3 0 2 0
After:  [4, 2, 2, 0]

Before: [0, 0, 0, 2]
12 2 3 1
After:  [0, 1, 0, 2]

Before: [3, 1, 3, 3]
9 3 0 1
After:  [3, 1, 3, 3]

Before: [1, 0, 2, 1]
11 3 2 3
After:  [1, 0, 2, 1]

Before: [2, 1, 0, 0]
14 0 3 2
After:  [2, 1, 1, 0]

Before: [3, 0, 2, 2]
10 1 0 1
After:  [3, 0, 2, 2]

Before: [2, 2, 1, 1]
1 2 3 1
After:  [2, 2, 1, 1]

Before: [0, 2, 2, 3]
15 1 3 2
After:  [0, 2, 0, 3]

Before: [1, 3, 0, 3]
2 0 2 2
After:  [1, 3, 0, 3]

Before: [3, 1, 2, 1]
11 3 2 0
After:  [1, 1, 2, 1]

Before: [2, 1, 2, 1]
11 3 2 0
After:  [1, 1, 2, 1]

Before: [1, 1, 2, 3]
8 0 2 1
After:  [1, 0, 2, 3]

Before: [2, 1, 2, 3]
5 1 2 0
After:  [0, 1, 2, 3]

Before: [1, 1, 0, 2]
7 3 3 1
After:  [1, 0, 0, 2]

Before: [0, 0, 2, 3]
15 2 3 2
After:  [0, 0, 0, 3]

Before: [1, 3, 0, 0]
2 0 2 0
After:  [0, 3, 0, 0]

Before: [3, 2, 2, 2]
9 2 1 3
After:  [3, 2, 2, 1]

Before: [2, 3, 3, 0]
12 3 2 3
After:  [2, 3, 3, 1]

Before: [3, 0, 1, 1]
7 2 3 0
After:  [0, 0, 1, 1]

Before: [3, 1, 3, 0]
0 1 2 0
After:  [0, 1, 3, 0]

Before: [0, 2, 2, 1]
11 3 2 2
After:  [0, 2, 1, 1]

Before: [1, 1, 1, 3]
15 1 3 2
After:  [1, 1, 0, 3]

Before: [2, 3, 3, 1]
9 2 3 2
After:  [2, 3, 0, 1]

Before: [0, 2, 0, 3]
6 0 0 0
After:  [0, 2, 0, 3]

Before: [2, 3, 1, 0]
14 0 3 0
After:  [1, 3, 1, 0]

Before: [2, 3, 2, 0]
14 0 3 2
After:  [2, 3, 1, 0]

Before: [0, 3, 1, 1]
6 0 0 2
After:  [0, 3, 0, 1]

Before: [2, 0, 1, 1]
1 2 3 3
After:  [2, 0, 1, 2]

Before: [1, 2, 1, 3]
1 2 0 1
After:  [1, 2, 1, 3]

Before: [3, 1, 2, 1]
5 1 2 2
After:  [3, 1, 0, 1]

Before: [1, 3, 2, 3]
8 0 2 0
After:  [0, 3, 2, 3]

Before: [3, 1, 0, 1]
4 3 1 0
After:  [0, 1, 0, 1]

Before: [0, 3, 2, 1]
11 3 2 1
After:  [0, 1, 2, 1]

Before: [2, 1, 3, 2]
0 1 2 2
After:  [2, 1, 0, 2]

Before: [2, 2, 1, 0]
14 0 3 0
After:  [1, 2, 1, 0]

Before: [1, 2, 2, 1]
11 3 2 1
After:  [1, 1, 2, 1]

Before: [2, 2, 2, 0]
14 0 3 3
After:  [2, 2, 2, 1]

Before: [3, 1, 1, 1]
1 2 3 3
After:  [3, 1, 1, 2]

Before: [1, 2, 2, 1]
11 3 2 0
After:  [1, 2, 2, 1]

Before: [3, 3, 0, 2]
4 0 2 1
After:  [3, 1, 0, 2]

Before: [0, 1, 0, 1]
6 0 0 1
After:  [0, 0, 0, 1]

Before: [3, 3, 2, 3]
9 3 0 0
After:  [1, 3, 2, 3]

Before: [0, 2, 1, 3]
13 0 2 3
After:  [0, 2, 1, 0]

Before: [0, 2, 1, 1]
6 0 0 3
After:  [0, 2, 1, 0]

Before: [1, 2, 0, 0]
2 0 2 3
After:  [1, 2, 0, 0]

Before: [2, 1, 0, 2]
7 3 3 0
After:  [0, 1, 0, 2]

Before: [3, 1, 2, 1]
11 3 2 3
After:  [3, 1, 2, 1]

Before: [0, 2, 0, 1]
6 0 0 2
After:  [0, 2, 0, 1]

Before: [1, 2, 2, 1]
8 0 2 3
After:  [1, 2, 2, 0]

Before: [0, 0, 2, 2]
6 0 0 0
After:  [0, 0, 2, 2]

Before: [0, 2, 3, 1]
6 0 0 2
After:  [0, 2, 0, 1]

Before: [3, 2, 0, 2]
12 2 3 3
After:  [3, 2, 0, 1]

Before: [2, 1, 3, 0]
12 3 2 1
After:  [2, 1, 3, 0]

Before: [3, 1, 1, 0]
4 2 1 1
After:  [3, 0, 1, 0]

Before: [2, 1, 2, 1]
11 3 2 3
After:  [2, 1, 2, 1]

Before: [1, 0, 2, 0]
8 0 2 1
After:  [1, 0, 2, 0]

Before: [3, 0, 2, 0]
3 2 2 0
After:  [4, 0, 2, 0]

Before: [2, 2, 1, 3]
15 2 3 2
After:  [2, 2, 0, 3]

Before: [1, 0, 3, 1]
7 3 3 1
After:  [1, 0, 3, 1]

Before: [0, 1, 2, 1]
11 3 2 2
After:  [0, 1, 1, 1]

Before: [1, 0, 1, 0]
1 2 0 1
After:  [1, 2, 1, 0]

Before: [0, 1, 3, 3]
13 0 1 1
After:  [0, 0, 3, 3]

Before: [1, 3, 0, 0]
2 0 2 2
After:  [1, 3, 0, 0]

Before: [0, 1, 1, 1]
13 0 1 0
After:  [0, 1, 1, 1]

Before: [1, 0, 1, 2]
1 2 0 2
After:  [1, 0, 2, 2]

Before: [0, 3, 2, 1]
13 0 1 3
After:  [0, 3, 2, 0]

Before: [2, 0, 0, 0]
14 0 3 2
After:  [2, 0, 1, 0]

Before: [1, 1, 1, 1]
1 2 0 0
After:  [2, 1, 1, 1]

Before: [3, 0, 1, 3]
10 1 0 1
After:  [3, 0, 1, 3]

Before: [1, 2, 1, 2]
7 3 3 1
After:  [1, 0, 1, 2]

Before: [0, 1, 2, 2]
5 1 2 1
After:  [0, 0, 2, 2]

Before: [0, 0, 2, 1]
6 0 0 0
After:  [0, 0, 2, 1]

Before: [1, 1, 0, 2]
2 0 2 3
After:  [1, 1, 0, 0]

Before: [2, 2, 3, 0]
14 0 3 2
After:  [2, 2, 1, 0]

Before: [1, 1, 3, 1]
0 1 2 2
After:  [1, 1, 0, 1]

Before: [1, 3, 1, 1]
7 3 3 0
After:  [0, 3, 1, 1]

Before: [0, 0, 3, 0]
6 0 0 1
After:  [0, 0, 3, 0]

Before: [3, 1, 3, 0]
0 1 2 1
After:  [3, 0, 3, 0]

Before: [1, 2, 2, 1]
8 0 2 1
After:  [1, 0, 2, 1]

Before: [1, 2, 0, 3]
2 0 2 2
After:  [1, 2, 0, 3]

Before: [1, 1, 0, 2]
12 2 3 1
After:  [1, 1, 0, 2]

Before: [0, 0, 3, 0]
12 3 2 2
After:  [0, 0, 1, 0]

Before: [1, 2, 0, 2]
2 0 2 3
After:  [1, 2, 0, 0]

Before: [0, 2, 3, 1]
13 0 3 3
After:  [0, 2, 3, 0]

Before: [0, 2, 2, 1]
11 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 3, 2, 2]
8 0 2 3
After:  [1, 3, 2, 0]

Before: [1, 1, 1, 3]
1 2 0 1
After:  [1, 2, 1, 3]

Before: [3, 0, 0, 1]
10 1 0 0
After:  [0, 0, 0, 1]

Before: [2, 1, 1, 1]
7 2 3 0
After:  [0, 1, 1, 1]

Before: [0, 1, 2, 2]
5 1 2 0
After:  [0, 1, 2, 2]

Before: [0, 2, 1, 2]
6 0 0 1
After:  [0, 0, 1, 2]

Before: [0, 3, 3, 1]
7 3 3 2
After:  [0, 3, 0, 1]

Before: [1, 1, 2, 1]
8 0 2 1
After:  [1, 0, 2, 1]

Before: [1, 1, 2, 1]
11 3 2 3
After:  [1, 1, 2, 1]

Before: [0, 1, 1, 3]
13 0 2 2
After:  [0, 1, 0, 3]

Before: [2, 2, 2, 2]
3 1 2 0
After:  [4, 2, 2, 2]

Before: [0, 3, 1, 1]
1 2 3 0
After:  [2, 3, 1, 1]

Before: [1, 1, 0, 3]
2 0 2 2
After:  [1, 1, 0, 3]

Before: [2, 1, 3, 1]
0 1 2 0
After:  [0, 1, 3, 1]

Before: [1, 1, 0, 0]
2 0 2 1
After:  [1, 0, 0, 0]

Before: [3, 2, 1, 1]
1 2 3 2
After:  [3, 2, 2, 1]

Before: [2, 3, 2, 3]
9 2 0 3
After:  [2, 3, 2, 1]

Before: [0, 0, 0, 1]
6 0 0 3
After:  [0, 0, 0, 0]

Before: [2, 2, 3, 3]
15 1 3 3
After:  [2, 2, 3, 0]

Before: [1, 0, 2, 3]
8 0 2 3
After:  [1, 0, 2, 0]

Before: [1, 1, 0, 2]
2 0 2 0
After:  [0, 1, 0, 2]

Before: [1, 1, 0, 2]
2 0 2 1
After:  [1, 0, 0, 2]

Before: [0, 0, 0, 1]
6 0 0 1
After:  [0, 0, 0, 1]

Before: [1, 3, 2, 1]
8 0 2 1
After:  [1, 0, 2, 1]

Before: [2, 0, 1, 0]
10 1 0 2
After:  [2, 0, 0, 0]

Before: [1, 2, 0, 1]
2 0 2 0
After:  [0, 2, 0, 1]

Before: [0, 2, 2, 3]
15 1 3 3
After:  [0, 2, 2, 0]

Before: [2, 1, 2, 3]
5 1 2 1
After:  [2, 0, 2, 3]

Before: [1, 3, 2, 1]
8 0 2 3
After:  [1, 3, 2, 0]

Before: [1, 1, 2, 2]
5 1 2 3
After:  [1, 1, 2, 0]

Before: [0, 1, 2, 1]
4 3 1 1
After:  [0, 0, 2, 1]

Before: [3, 1, 3, 0]
0 1 2 2
After:  [3, 1, 0, 0]

Before: [2, 0, 2, 2]
3 0 2 0
After:  [4, 0, 2, 2]

Before: [0, 1, 3, 1]
0 1 2 0
After:  [0, 1, 3, 1]

Before: [2, 1, 2, 2]
5 1 2 1
After:  [2, 0, 2, 2]

Before: [1, 3, 0, 0]
2 0 2 3
After:  [1, 3, 0, 0]

Before: [1, 2, 2, 3]
3 2 2 0
After:  [4, 2, 2, 3]

Before: [0, 3, 2, 0]
6 0 0 2
After:  [0, 3, 0, 0]

Before: [0, 3, 2, 3]
13 0 3 3
After:  [0, 3, 2, 0]

Before: [3, 0, 0, 0]
4 0 2 3
After:  [3, 0, 0, 1]

Before: [2, 3, 2, 2]
4 3 2 1
After:  [2, 0, 2, 2]

Before: [2, 2, 2, 0]
3 0 2 2
After:  [2, 2, 4, 0]

Before: [3, 0, 3, 3]
9 3 0 3
After:  [3, 0, 3, 1]

Before: [0, 1, 2, 2]
13 0 1 3
After:  [0, 1, 2, 0]

Before: [1, 1, 1, 1]
1 2 3 3
After:  [1, 1, 1, 2]

Before: [2, 2, 3, 2]
4 2 0 0
After:  [1, 2, 3, 2]

Before: [3, 1, 3, 3]
15 1 3 0
After:  [0, 1, 3, 3]

Before: [0, 1, 1, 3]
6 0 0 1
After:  [0, 0, 1, 3]

Before: [0, 3, 1, 1]
6 0 0 1
After:  [0, 0, 1, 1]

Before: [3, 0, 0, 3]
9 3 0 2
After:  [3, 0, 1, 3]

Before: [0, 3, 3, 1]
9 2 3 2
After:  [0, 3, 0, 1]

Before: [2, 0, 1, 0]
14 0 3 3
After:  [2, 0, 1, 1]

Before: [0, 2, 3, 0]
6 0 0 3
After:  [0, 2, 3, 0]

Before: [1, 3, 0, 2]
2 0 2 1
After:  [1, 0, 0, 2]

Before: [1, 1, 2, 1]
11 3 2 0
After:  [1, 1, 2, 1]

Before: [1, 1, 2, 3]
8 0 2 0
After:  [0, 1, 2, 3]

Before: [3, 1, 2, 2]
5 1 2 3
After:  [3, 1, 2, 0]

Before: [1, 0, 0, 2]
2 0 2 2
After:  [1, 0, 0, 2]

Before: [2, 0, 3, 0]
12 3 2 3
After:  [2, 0, 3, 1]

Before: [1, 1, 2, 1]
8 0 2 3
After:  [1, 1, 2, 0]

Before: [1, 1, 2, 0]
8 0 2 1
After:  [1, 0, 2, 0]

Before: [3, 1, 2, 2]
5 1 2 0
After:  [0, 1, 2, 2]

Before: [1, 2, 2, 2]
8 0 2 3
After:  [1, 2, 2, 0]

Before: [3, 3, 0, 0]
10 2 0 2
After:  [3, 3, 0, 0]

Before: [0, 3, 2, 2]
6 0 0 2
After:  [0, 3, 0, 2]

Before: [3, 0, 3, 1]
10 1 0 0
After:  [0, 0, 3, 1]

Before: [2, 3, 1, 1]
7 2 3 1
After:  [2, 0, 1, 1]

Before: [3, 1, 2, 3]
3 2 2 1
After:  [3, 4, 2, 3]

Before: [0, 2, 2, 3]
15 1 3 1
After:  [0, 0, 2, 3]

Before: [0, 3, 2, 1]
6 0 0 0
After:  [0, 3, 2, 1]

Before: [0, 1, 3, 0]
6 0 0 3
After:  [0, 1, 3, 0]

Before: [1, 3, 2, 1]
7 3 3 1
After:  [1, 0, 2, 1]

Before: [1, 0, 0, 1]
2 0 2 1
After:  [1, 0, 0, 1]

Before: [3, 1, 0, 2]
12 2 3 3
After:  [3, 1, 0, 1]

Before: [3, 0, 2, 3]
10 1 0 0
After:  [0, 0, 2, 3]

Before: [3, 2, 2, 1]
11 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 1, 2, 3]
5 1 2 1
After:  [1, 0, 2, 3]

Before: [1, 1, 0, 1]
2 0 2 3
After:  [1, 1, 0, 0]

Before: [2, 1, 2, 2]
5 1 2 0
After:  [0, 1, 2, 2]

Before: [0, 3, 3, 1]
6 0 0 3
After:  [0, 3, 3, 0]

Before: [3, 2, 2, 3]
9 2 1 3
After:  [3, 2, 2, 1]

Before: [1, 1, 2, 1]
8 0 2 0
After:  [0, 1, 2, 1]

Before: [2, 2, 1, 0]
14 0 3 2
After:  [2, 2, 1, 0]

Before: [3, 2, 2, 3]
9 2 1 2
After:  [3, 2, 1, 3]

Before: [1, 2, 2, 2]
8 0 2 2
After:  [1, 2, 0, 2]

Before: [1, 0, 2, 2]
8 0 2 0
After:  [0, 0, 2, 2]

Before: [1, 3, 0, 1]
2 0 2 1
After:  [1, 0, 0, 1]

Before: [3, 2, 3, 3]
15 1 3 3
After:  [3, 2, 3, 0]

Before: [0, 2, 0, 3]
6 0 0 1
After:  [0, 0, 0, 3]

Before: [2, 1, 3, 1]
0 1 2 1
After:  [2, 0, 3, 1]

Before: [1, 3, 0, 1]
2 0 2 0
After:  [0, 3, 0, 1]

Before: [2, 1, 2, 1]
5 1 2 1
After:  [2, 0, 2, 1]

Before: [1, 3, 0, 2]
12 2 3 2
After:  [1, 3, 1, 2]

Before: [0, 3, 0, 1]
13 0 1 2
After:  [0, 3, 0, 1]

Before: [3, 3, 0, 1]
7 3 3 3
After:  [3, 3, 0, 0]

Before: [0, 3, 0, 0]
13 0 1 2
After:  [0, 3, 0, 0]

Before: [2, 1, 1, 0]
4 2 1 3
After:  [2, 1, 1, 0]

Before: [3, 0, 0, 3]
10 1 0 1
After:  [3, 0, 0, 3]

Before: [2, 0, 2, 3]
15 2 3 0
After:  [0, 0, 2, 3]

Before: [1, 0, 0, 2]
2 0 2 3
After:  [1, 0, 0, 0]

Before: [1, 1, 0, 3]
2 0 2 0
After:  [0, 1, 0, 3]

Before: [3, 0, 0, 0]
10 2 0 3
After:  [3, 0, 0, 0]

Before: [3, 0, 2, 1]
11 3 2 0
After:  [1, 0, 2, 1]

Before: [3, 0, 0, 3]
10 2 0 2
After:  [3, 0, 0, 3]



13 0 0 0
3 0 2 0
8 3 0 1
13 0 0 3
3 3 1 3
4 0 1 0
13 0 1 0
1 2 0 2
8 2 1 3
8 1 2 0
13 0 0 1
3 1 0 1
2 0 3 1
13 1 3 1
13 1 3 1
1 2 1 2
11 2 0 0
8 3 0 2
8 3 2 1
8 0 0 3
12 3 2 2
13 2 2 2
13 2 1 2
1 0 2 0
11 0 3 1
8 3 1 3
8 0 2 2
8 0 3 0
0 3 2 3
13 3 1 3
1 1 3 1
11 1 1 3
8 3 1 0
8 0 2 1
13 3 0 2
3 2 2 2
4 2 0 1
13 1 3 1
1 3 1 3
11 3 2 1
8 0 2 3
8 1 0 0
15 3 2 2
13 2 3 2
1 1 2 1
11 1 2 3
8 3 0 1
8 2 0 2
11 0 2 2
13 2 3 2
1 2 3 3
11 3 2 0
13 2 0 2
3 2 3 2
8 3 1 3
0 3 2 3
13 3 1 3
1 3 0 0
11 0 3 1
8 2 2 3
8 2 1 2
8 3 0 0
4 2 0 3
13 3 1 3
1 3 1 1
11 1 0 2
8 3 3 3
8 2 2 0
13 1 0 1
3 1 0 1
5 3 0 3
13 3 1 3
1 2 3 2
11 2 3 1
8 1 1 0
8 0 2 3
8 2 0 2
11 0 2 3
13 3 1 3
1 3 1 1
13 2 0 3
3 3 3 3
8 2 3 0
13 2 0 2
3 2 3 2
7 0 2 3
13 3 3 3
1 3 1 1
8 2 0 2
13 3 0 3
3 3 1 3
2 3 0 0
13 0 2 0
13 0 1 0
1 1 0 1
8 2 3 0
8 2 0 3
10 2 3 2
13 2 3 2
13 2 3 2
1 2 1 1
11 1 1 0
8 0 1 1
8 1 0 3
13 2 0 2
3 2 0 2
3 3 1 3
13 3 3 3
1 0 3 0
11 0 2 2
8 2 0 3
13 0 0 0
3 0 2 0
9 0 3 0
13 0 1 0
13 0 2 0
1 2 0 2
8 3 1 1
8 3 2 3
8 2 1 0
5 1 0 0
13 0 1 0
1 2 0 2
11 2 1 3
8 2 3 0
13 1 0 2
3 2 2 2
8 1 2 1
2 1 0 2
13 2 3 2
1 3 2 3
11 3 3 2
8 1 3 0
8 3 0 3
1 1 0 3
13 3 3 3
1 2 3 2
11 2 2 1
8 3 3 3
8 2 2 2
11 0 2 0
13 0 2 0
13 0 3 0
1 0 1 1
11 1 1 0
8 2 3 3
8 2 1 1
10 1 3 3
13 3 2 3
1 0 3 0
11 0 2 2
8 1 2 0
8 3 2 3
1 0 0 3
13 3 2 3
13 3 1 3
1 2 3 2
11 2 2 0
8 1 1 1
13 2 0 2
3 2 2 2
13 2 0 3
3 3 0 3
15 3 2 1
13 1 1 1
13 1 2 1
1 1 0 0
11 0 0 3
8 1 1 2
13 0 0 1
3 1 2 1
8 3 3 0
0 0 2 0
13 0 1 0
13 0 2 0
1 3 0 3
11 3 0 0
8 1 3 1
8 2 0 3
8 0 1 2
13 1 2 3
13 3 1 3
1 3 0 0
13 1 0 3
3 3 0 3
8 3 0 2
8 0 2 1
12 3 2 3
13 3 1 3
13 3 2 3
1 0 3 0
11 0 3 2
8 0 0 3
13 1 0 0
3 0 1 0
8 2 1 1
10 1 3 1
13 1 2 1
1 1 2 2
11 2 1 3
8 2 0 2
8 2 3 1
11 0 2 2
13 2 2 2
13 2 2 2
1 2 3 3
11 3 3 2
8 1 0 3
13 0 0 1
3 1 0 1
3 3 1 3
13 3 1 3
1 3 2 2
11 2 3 1
8 2 1 2
8 2 3 3
11 0 2 2
13 2 1 2
1 2 1 1
11 1 2 2
8 1 0 3
13 3 0 0
3 0 2 0
8 0 1 1
14 0 3 1
13 1 3 1
1 1 2 2
11 2 2 1
8 1 1 0
8 3 1 2
1 0 0 0
13 0 1 0
1 0 1 1
13 2 0 0
3 0 3 0
13 3 0 2
3 2 1 2
8 0 3 3
0 0 2 2
13 2 1 2
1 1 2 1
11 1 3 0
8 1 1 3
8 2 1 2
8 3 3 1
3 3 1 3
13 3 2 3
1 3 0 0
8 1 0 2
8 2 1 1
8 0 3 3
10 1 3 1
13 1 1 1
1 0 1 0
11 0 3 3
8 3 0 1
8 1 1 0
8 0 1 2
3 0 1 2
13 2 1 2
1 2 3 3
13 2 0 2
3 2 3 2
8 2 2 0
5 1 0 2
13 2 2 2
1 3 2 3
11 3 0 0
8 2 2 2
8 2 1 3
5 1 3 3
13 3 1 3
1 3 0 0
11 0 1 1
8 3 0 2
8 1 2 0
8 0 1 3
8 2 3 3
13 3 3 3
1 3 1 1
8 2 3 2
8 3 3 0
8 1 3 3
6 2 0 0
13 0 2 0
13 0 1 0
1 1 0 1
11 1 3 3
8 1 2 0
13 2 0 1
3 1 3 1
4 2 1 2
13 2 1 2
1 2 3 3
8 3 0 0
8 2 3 2
4 2 0 1
13 1 1 1
1 3 1 3
11 3 1 0
8 2 3 1
8 0 1 3
15 3 2 1
13 1 1 1
13 1 1 1
1 1 0 0
11 0 1 1
8 0 3 0
15 3 2 3
13 3 2 3
13 3 3 3
1 1 3 1
13 3 0 0
3 0 2 0
8 0 2 2
13 1 0 3
3 3 1 3
13 3 2 0
13 0 3 0
1 1 0 1
8 0 0 3
8 3 2 0
7 2 0 0
13 0 3 0
1 0 1 1
11 1 1 2
8 1 0 0
8 1 1 3
8 1 2 1
1 3 0 3
13 3 3 3
1 3 2 2
11 2 1 3
8 0 2 1
8 0 3 2
13 0 2 1
13 1 1 1
13 1 1 1
1 3 1 3
11 3 1 1
8 3 3 2
8 0 3 3
8 2 0 0
10 0 3 3
13 3 2 3
1 3 1 1
11 1 0 3
8 2 2 1
8 2 2 2
8 3 1 0
4 2 0 2
13 2 1 2
1 3 2 3
8 1 0 0
13 2 0 2
3 2 0 2
8 1 1 1
1 0 0 0
13 0 1 0
1 3 0 3
11 3 3 1
8 2 2 3
8 2 2 0
9 0 3 3
13 3 2 3
13 3 2 3
1 1 3 1
11 1 3 3
8 1 3 0
8 3 1 1
8 2 3 2
11 0 2 0
13 0 1 0
1 0 3 3
11 3 1 0
8 3 2 3
13 0 0 1
3 1 2 1
8 1 3 2
0 3 2 2
13 2 3 2
13 2 2 2
1 2 0 0
11 0 0 1
8 3 1 0
8 2 0 3
8 0 0 2
7 2 0 2
13 2 3 2
13 2 2 2
1 1 2 1
11 1 3 3
8 2 1 2
8 1 2 0
8 0 2 1
11 0 2 0
13 0 2 0
1 3 0 3
11 3 3 2
8 2 2 0
8 0 0 3
10 0 3 0
13 0 1 0
1 2 0 2
11 2 1 3
8 2 2 0
8 1 1 1
8 3 3 2
13 1 2 0
13 0 3 0
13 0 3 0
1 0 3 3
11 3 0 1
8 1 0 3
8 2 3 0
7 0 2 0
13 0 1 0
1 1 0 1
11 1 3 2
8 2 1 0
13 2 0 1
3 1 3 1
14 0 3 3
13 3 1 3
1 3 2 2
11 2 0 0
8 2 2 1
13 0 0 2
3 2 0 2
13 0 0 3
3 3 2 3
12 2 3 2
13 2 1 2
13 2 2 2
1 2 0 0
11 0 0 1
13 2 0 3
3 3 1 3
8 3 3 2
8 2 2 0
14 0 3 2
13 2 1 2
13 2 2 2
1 2 1 1
11 1 0 0
8 3 1 3
13 1 0 2
3 2 3 2
13 0 0 1
3 1 2 1
6 1 2 1
13 1 1 1
1 0 1 0
11 0 1 2
8 2 1 0
8 1 1 3
8 0 2 1
2 3 0 0
13 0 2 0
13 0 1 0
1 0 2 2
11 2 3 0
8 3 1 3
8 3 1 1
8 2 2 2
4 2 1 3
13 3 2 3
13 3 3 3
1 3 0 0
8 3 3 2
13 0 0 3
3 3 3 3
8 1 3 1
13 1 2 2
13 2 2 2
13 2 2 2
1 0 2 0
11 0 3 2
8 2 2 0
13 0 0 1
3 1 2 1
8 2 2 3
10 0 3 1
13 1 2 1
1 1 2 2
11 2 3 3
13 3 0 0
3 0 3 0
8 0 1 2
8 3 2 1
7 2 0 1
13 1 2 1
1 3 1 3
13 2 0 1
3 1 1 1
7 2 0 0
13 0 1 0
13 0 3 0
1 3 0 3
11 3 3 1
8 2 1 2
8 3 2 3
13 0 0 0
3 0 3 0
4 2 0 0
13 0 2 0
1 1 0 1
11 1 3 3
8 1 3 2
8 2 3 0
8 3 3 1
5 1 0 0
13 0 1 0
1 0 3 3
8 2 0 2
8 1 0 0
8 0 0 1
11 0 2 2
13 2 3 2
1 3 2 3
11 3 0 1
13 0 0 0
3 0 2 0
8 2 1 3
8 3 2 2
9 0 3 3
13 3 2 3
1 3 1 1
11 1 1 3
8 3 3 1
8 2 2 2
13 2 0 0
3 0 1 0
4 2 1 0
13 0 3 0
1 3 0 3
11 3 0 1
13 1 0 3
3 3 1 3
13 0 0 2
3 2 3 2
8 1 2 0
13 0 2 3
13 3 1 3
13 3 3 3
1 1 3 1
11 1 3 0
8 0 2 1
8 0 1 3
8 2 3 2
13 2 1 2
1 2 0 0
13 3 0 2
3 2 2 2
13 2 0 1
3 1 3 1
4 2 1 1
13 1 3 1
1 0 1 0
11 0 0 1
8 1 2 2
8 2 3 0
8 3 0 2
13 2 2 2
1 2 1 1
11 1 1 0
8 1 0 1
8 1 1 2
8 1 3 3
1 3 3 2
13 2 2 2
1 0 2 0
11 0 1 1
8 3 2 0
8 2 3 2
8 0 0 3
4 2 0 3
13 3 3 3
1 1 3 1
11 1 0 0
8 3 2 2
8 0 0 1
8 3 0 3
8 2 3 3
13 3 1 3
1 3 0 0
11 0 0 2
13 2 0 0
3 0 2 0
8 1 0 1
8 2 1 3
9 0 3 1
13 1 1 1
13 1 2 1
1 2 1 2
11 2 2 0
8 3 0 1
8 1 0 2
0 1 2 2
13 2 3 2
13 2 3 2
1 2 0 0
8 2 2 1
8 2 1 2
8 0 0 3
15 3 2 3
13 3 1 3
1 3 0 0
11 0 2 3
8 3 3 0
8 3 3 2
8 0 1 1
0 0 2 0
13 0 2 0
13 0 2 0
1 3 0 3
11 3 1 1
8 2 0 0
8 3 2 3
7 0 2 2
13 2 2 2
1 1 2 1
11 1 1 0
8 0 3 3
13 1 0 2
3 2 2 2
8 0 0 1
15 3 2 1
13 1 3 1
1 0 1 0
11 0 0 1
8 3 3 0
13 3 0 2
3 2 1 2
8 1 1 3
1 3 3 0
13 0 2 0
1 0 1 1
11 1 1 0
8 3 0 3
13 0 0 2
3 2 3 2
8 2 2 1
8 2 3 1
13 1 2 1
1 1 0 0
11 0 0 2
8 2 2 0
8 1 2 1
8 1 2 3
2 3 0 3
13 3 2 3
1 3 2 2
8 3 0 1
13 1 0 3
3 3 2 3
9 0 3 1
13 1 2 1
13 1 2 1
1 1 2 2
8 1 3 0
8 2 3 1
10 1 3 3
13 3 1 3
1 2 3 2
11 2 1 1
8 2 1 3
8 3 3 2
1 0 0 2
13 2 3 2
1 1 2 1
8 2 2 0
13 3 0 2
3 2 2 2
9 0 3 3
13 3 1 3
1 3 1 1
8 2 2 3
8 1 2 2
13 0 0 0
3 0 1 0
2 0 3 2
13 2 1 2
1 1 2 1
8 0 1 0
8 3 3 2
8 3 0 2
13 2 1 2
1 2 1 1
11 1 1 2
8 3 0 0
8 0 1 1
5 0 3 1
13 1 1 1
13 1 1 1
1 1 2 2
11 2 0 1
13 2 0 0
3 0 1 0
8 3 0 2
8 0 2 3
12 3 2 0
13 0 1 0
1 0 1 1
11 1 2 0
8 3 0 1
13 1 0 2
3 2 0 2
8 3 2 3
8 2 1 1
13 1 3 1
13 1 3 1
1 1 0 0
11 0 3 1
8 0 3 3
8 3 2 2
8 1 1 0
12 3 2 2
13 2 3 2
13 2 2 2
1 2 1 1
11 1 0 3
13 0 0 0
3 0 0 0
8 1 2 1
13 1 0 2
3 2 0 2
8 2 1 0
13 0 2 0
1 0 3 3
11 3 1 0
13 0 0 3
3 3 0 3
8 3 3 1
13 3 0 2
3 2 2 2
15 3 2 2
13 2 2 2
13 2 2 2
1 0 2 0
8 1 0 1
8 0 3 2
8 2 2 3
2 1 3 1
13 1 2 1
1 1 0 0
11 0 2 1
8 2 2 2
8 2 3 0
9 0 3 0
13 0 1 0
13 0 3 0
1 1 0 1
8 0 2 0
13 3 0 2
3 2 0 2
12 2 3 2
13 2 3 2
13 2 1 2
1 2 1 1
11 1 2 0
13 3 0 2
3 2 1 2
8 2 1 1
8 0 0 3
10 1 3 2
13 2 1 2
13 2 2 2
1 0 2 0
11 0 3 3
8 1 1 1
8 3 2 0
8 3 0 2
13 1 2 0
13 0 2 0
1 3 0 3
11 3 3 0
8 2 0 1
8 0 2 3
6 1 2 2
13 2 2 2
1 2 0 0
11 0 2 2
8 0 0 1
8 2 1 0
8 3 0 0
13 0 1 0
13 0 2 0
1 0 2 2
11 2 3 3
8 3 3 2
8 3 0 1
8 2 1 0
4 0 1 2
13 2 3 2
1 3 2 3
11 3 2 2
8 2 2 3
13 1 0 1
3 1 2 1
10 1 3 3
13 3 3 3
1 2 3 2
11 2 3 3
8 0 3 0
8 0 1 2
8 3 3 1
0 1 2 1
13 1 1 1
13 1 2 1
1 1 3 3
11 3 1 2
8 1 1 1
13 2 0 3
3 3 2 3
2 1 3 1
13 1 2 1
13 1 2 1
1 2 1 2
11 2 1 3
8 2 2 2
13 2 0 1
3 1 0 1
8 3 3 0
6 2 0 2
13 2 1 2
13 2 3 2
1 3 2 3
11 3 2 0
13 0 0 3
3 3 0 3
8 3 0 2
8 3 2 1
12 3 2 1
13 1 3 1
13 1 2 1
1 0 1 0
11 0 2 2
8 1 2 1
8 2 0 0
10 0 3 3
13 3 2 3
1 3 2 2
11 2 1 1
8 2 1 3
8 3 0 2
6 0 2 3
13 3 1 3
13 3 2 3
1 3 1 1
11 1 1 2
13 2 0 3
3 3 1 3
8 0 2 1
14 0 3 0
13 0 1 0
1 2 0 2
11 2 3 0
8 1 0 2
8 2 3 3
8 1 3 3
13 3 2 3
13 3 2 3
1 3 0 0
11 0 0 3
8 3 1 2
13 0 0 0
3 0 2 0
7 0 2 2
13 2 1 2
1 2 3 3
11 3 1 1
8 2 0 2
8 0 0 0
8 1 1 3
8 3 0 2
13 2 1 2
1 1 2 1
11 1 0 0
8 2 0 3
8 1 1 1
13 1 0 2
3 2 3 2
2 1 3 2
13 2 2 2
1 2 0 0
8 3 2 1
8 0 0 2
5 1 3 2
13 2 3 2
1 0 2 0
11 0 2 3
8 2 2 2
8 2 1 0
8 1 3 1
2 1 0 0
13 0 1 0
1 3 0 3
11 3 0 1
8 2 1 3
13 0 0 2
3 2 1 2
8 1 1 0
1 0 0 3
13 3 3 3
1 3 1 1
8 2 0 0
8 2 3 3
13 2 0 2
3 2 0 2
9 0 3 0
13 0 3 0
1 0 1 1
11 1 3 0
8 2 2 2
8 0 3 3
8 0 1 1
15 3 2 2
13 2 3 2
1 0 2 0
11 0 2 3
8 3 2 0
13 3 0 2
3 2 2 2
6 2 0 0
13 0 1 0
1 0 3 3
11 3 3 0
8 3 3 3
8 0 3 2
8 2 2 1
5 3 1 2
13 2 3 2
13 2 1 2
1 0 2 0
11 0 0 1
8 2 0 0
8 0 0 3
8 0 0 2
10 0 3 3
13 3 1 3
1 3 1 1
11 1 2 3
8 3 3 2
8 0 1 1
8 2 1 1
13 1 1 1
13 1 1 1
1 3 1 3
11 3 1 0""" 
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
  funcs=["addr","addi","mulr","muli","banr","bani","borr","bori",\
         "setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]
  funcs=[locals()[i] for i in funcs]
  threeOrMore=0
  regex=r"(B\w+.*)\n(.*)\n(A\w+.*)"
  pattern=re.compile(regex)
  part1=[list(i) for i in pattern.findall(input)]
  regex=r"\d+"
  pattern=re.compile(regex)
  for row in range(len(part1)):
    for col in range(3):
      part1[row][col]=map(int,pattern.findall(part1[row][col]))
  separator=re.search(r"\n\n\n\n",input).start()
  part2=[map(int,i.split()) for i in input[separator:].split('\n')[4:]]
  #iterate part1
  for sample in part1:
    correct=0
    before, instruction, after = [ row[:] for row in sample]
    for f in funcs:
      args=instruction[1:]+[before[:]]
      if f(*args)==after:
        correct+=1
    if correct>=3:
      threeOrMore+=1
  print "There's",threeOrMore,"samples that match 3 or more opcodes."
except Exception as e:
  print "in main:",str(e),sys.exc_info()[2].tb_lineno
finally:
  raw_input()