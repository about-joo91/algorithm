import sys
import math
sys.stdin = open('/Users/jujeonghan/Developer/camp/algorithm_study/test.txt','r')
N, jimin, hansu = map(int, input().split())
cnt = 0
def recursion(hansu, jimin):
    global cnt
    if hansu == jimin:
        return
    
    cnt+=1
    recursion(int(hansu/2), int(jimin/2))

recursion(hansu, jimin)
print(cnt)

