from copy import deepcopy
from collections import deque
def bfs(x, y, key, res, visit):
    q = deque()
    q.append((x, y, key))
    max_key = key
    while q:
        x, y, key = q.popleft()
        max_key = key
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] != "*" and (visit[nx][ny] == 0 or visit[nx][ny] != key):
                if 'a' <= Map[nx][ny] <= 'z':
                    if Map[nx][ny] not in key:
                        temp = deepcopy(key)
                        temp.add(Map[nx][ny])
                        visit[nx][ny] = temp
                        q = deque()
                        q.append((nx, ny, temp))
                        break
                    else:
                        visit[nx][ny] = key
                        q.append((nx, ny, key))
                elif "A" <= Map[nx][ny] <= "Z" and Map[nx][ny].lower() in key:
                    visit[nx][ny] = key
                    q.append((nx, ny, key))
                elif Map[nx][ny] == "$":
                    res.add((nx, ny))
                    visit[nx][ny] = key
                    q.append((nx, ny, key))
                elif Map[nx][ny] == ".":
                    visit[nx][ny] = key
                    q.append((nx, ny, key))
    return res, max_key


def solve(Map, key):
    # 벽 가능성 후보들 뽑기
    wall = []
    res = set()
    for j in range(M):
        if Map[0][j] != "*":
            wall.append((-1, j))
        if Map[N-1][j] != "*":
            wall.append((N, j))
    for i in range(N):
        if Map[i][0] != "*":
            wall.append((i, -1))
        if Map[i][M-1] != "*":
            wall.append((i, M))
    flag = 1 # key 업데이트 되는지 확인용
    visit = [[0]*M for _ in range(N)]
    while flag:
        pre_key = deepcopy(key)
        # 벽에대해서 반복문으로 BFS돌고
        for wx, wy in wall:
            res, key = bfs(wx, wy, key, res, visit)
        if pre_key == key:
            break
    return len(res)


steps= [(1, 0),(-1, 0),(0, 1),(0, -1)]
for tc in range(int(input())):
    N, M = map(int, input().split())
    Map = [list(input()) for _ in range(N)]
    key = set(list(input()))
    if "0" in key:
        key = set()
    res = solve(Map, key)
    print(res)