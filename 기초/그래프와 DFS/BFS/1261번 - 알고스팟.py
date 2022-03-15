from collections import deque
INF = int(1e10)
steps = [(1,0),(0,1),(-1,0),(0,-1)]
M, N = map(int, input().split())
graph = [list(map(int,list(input()))) for _ in range(N)]
visit = [[INF]*M for i in range(N)]
# 00 -> N-1 M - 1로 벽최소
q = deque()
# q.append((0,0,0)) # 벽갯수, x , y
q.append((0,0)) # x , y
visit[0][0] = 0
while q:
    x, y = q.popleft()
    if x == N - 1 and y == M - 1:
        print(visit[x][y])
        break
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0 and visit[nx][ny] > visit[x][y]:
                visit[nx][ny] = visit[x][y]
                q.appendleft((nx, ny))
            # 아 무슨 wall_cnt + 1 이 아닌 wall_cnt 넣었다고 메모리 초과뜨는 문제
            elif graph[nx][ny] == 1 and visit[nx][ny] > visit[x][y] + 1:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))