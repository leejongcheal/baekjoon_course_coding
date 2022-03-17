N, M = map(int,input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
res = 0
front = 0
rear = 0
right = 0
left = 0
bottom = N*M
for i in range(N):
    front += Map[i][0]
    for j in range(1, M):
        if Map[i][j] > Map[i][j-1]:
            front += Map[i][j] - Map[i][j-1]
    # rear += Map[i][M-1]
    # for j in range(M-2, -1, -1):
    #     if Map[i][j] > Map[i][j + 1]:
    #         rear = Map[i][j] - Map[i][j+1]

for j in range(M):
    left += Map[0][j]
    for i in range(1, N):
        if Map[i][j] > Map[i-1][j]:
            left += Map[i][j] - Map[i-1][j]
    # right += Map[N-1][j]
    # for i in range(N-2, -1,-1):
    #     if Map[i][j] > Map[i+1][j]:
    #         right += Map[i][j] - Map[i+1][j]
# res = front + rear + left + right + bottom*2
res = (front + left + bottom)*2
print(res)