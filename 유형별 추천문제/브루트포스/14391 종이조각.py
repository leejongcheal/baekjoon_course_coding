from collections import deque
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
res = 0
q = deque()
q.append((0, visit))
while q:
    flag = 0
    val, visit = q.popleft()
    # print(visit)
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0:
                flag = 1
                temp = [v[::] for v in visit]
                temp[i][j] = 1
                q.append((val + int(Map[i][j]), temp))
                x, y = i, j
                now = Map[i][j]
                for h in range(N):
                    if 0 <= x+1 < N and temp[x+1][y] == 0:
                        x += 1
                        temp = [t[::] for t in temp]
                        temp[x][y] = 1
                        now += Map[x][y]
                        q.append((val + int(now), temp))
                    else:
                        break
                x, y = i, j
                now = Map[i][j]
                temp = [v[::] for v in visit]
                temp[i][j] = 1
                for w in range(M):
                    if 0 <= y + 1 < M and temp[x][y+1] == 0:
                        y += 1
                        temp = [t[::] for t in temp]
                        temp[x][y] = 1
                        now += Map[x][y]
                        q.append((val + int(now), temp))
                    else:
                        break
            break
        if flag:
            break
    if flag == 0:
        res = max(res, val)
print(res)