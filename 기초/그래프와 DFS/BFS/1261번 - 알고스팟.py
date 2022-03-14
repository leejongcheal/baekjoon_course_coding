from collections import deque
import heapq
steps = [(1,0),(0,1),(-1,0),(0,-1)]
M, N = map(int, input().split())
graph = [list(map(int,list(input()))) for _ in range(N)]
visit = set() # x, y, 벽부신 갯수
# 00 -> N-1 M - 1로 벽최소
q = []
heapq.heappush(q,(0,0,0,0)) # 벽갯수, 이동갯수, x , y
visit.add((0,0,0))
while q:
    wall_cnt, move_cnt, x, y = heapq.heappop(q)
    if x == N - 1 and y == M - 1:
        print(wall_cnt)
        break
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and (wall_cnt, nx, ny) not in visit:
            if graph[nx][ny] == 0:
                visit.add((wall_cnt, nx, ny))
                heapq.heappush(q,(wall_cnt, move_cnt + 1, nx, ny))
            if graph[nx][ny] == 1:
                visit.add((wall_cnt + 1, nx, ny))
                heapq.heappush(q,(wall_cnt + 1, move_cnt + 1, nx, ny))