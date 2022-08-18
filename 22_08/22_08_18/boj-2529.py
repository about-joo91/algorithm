import sys

K = int(sys.stdin.readline())
inequality_sign = sys.stdin.readline().split()
visited =[False] * (10)
ans = []
def check(fir,sec,sign):
    if sign == '<':
        return fir < sec
    return fir > sec

def dfs(depth, answer):
    if depth == K+1:
        ans.append(answer)
        return
    for i in range(10):
        if not visited[i]:
            if len(answer) == 0 or check(answer[depth-1], str(i), inequality_sign[depth-1]):
                visited[i] = True
                dfs(depth+1, answer+str(i))
                visited[i] = False
            

dfs(0, '')
ans.sort()
print(ans[-1])
print(ans[0])