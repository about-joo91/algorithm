N = int(input())
papers = []
for _ in range(N):
    papers.append(list(map(int, input().split())))
colors = [0] *2
def check_colors(x, y, N):
    color = papers[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != papers[i][j]:
                check_colors(x, y, N//2)
                check_colors(x, y+N//2, N//2)
                check_colors(x+N//2, y, N//2)
                check_colors(x+N//2, y+N//2, N//2)
                return
    colors[color]+=1
check_colors(0,0,N)
print(colors[0])
print(colors[1])