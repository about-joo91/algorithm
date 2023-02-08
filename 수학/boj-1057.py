import math
N, jimin, hansu = map(int, input().split())
cnt = 0
def recursion(hansu, jimin):
    global cnt
    if hansu == jimin:
        return
    
    cnt+=1
    recursion(math.ceil(hansu/2), math.ceil(jimin/2))

recursion(hansu, jimin)
print(cnt)