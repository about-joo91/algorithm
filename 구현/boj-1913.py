import sys
input = sys.stdin.readline

N = int(input().rstrip()) 
Find = int(input().rstrip())
arr = [ [0 for _ in range(N)] for _ in range(N) ]
dy =[0,1,0,-1]
dx =[1,0,-1,0]
x ,y = 0,0
num = N * N -1
arr[x][y] = N * N


while True:    
    for i in range(4):   
      while True :
        x = x + dx[i]
        y = y + dy[i]
        if x >= N or y >= N or x <  0 or y < 0 or arr[x][y] != 0 :
            x -= dx[i]
            y -= dy[i]         
            break
        else:           
            arr[x][y] = num
            if arr[x][y] == Find:
                ans1, ans2 = x,y
            num -= 1            
    if x == N//2 and y == N//2:
        break


for i in arr:
    print(*i)         
print(ans1+1,ans2+1)
