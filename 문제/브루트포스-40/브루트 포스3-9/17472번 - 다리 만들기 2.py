from collections import deque, defaultdict
from copy import deepcopy
def island_number(x, y):
    global island_cnt
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == 1 and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            Map[nx][ny] = island_cnt
            group.append((nx, ny))
            island_number(nx, ny)
def check(graph):
    visit = [0]*island_cnt
    q = deque()
    q.append(1)
    visit[0] = 1
    while q:
        now = q.popleft()
        for next in graph[now]:
            if visit[next - 1] == 0:
                visit[next - 1] = 1
                q.append(next)
    if sum(visit) == island_cnt:
        return 1
    else:
        return 0

def connect_dfs(is_num, graph, connect):
    global res
    if check(graph):
        cnt = 0
        for x, y, nx, ny in connect:
            dx, dy = abs(x - nx), abs(y - ny)
            cnt += max(dx, dy) - 1
        res = min(res, cnt)
    visit = [0]*island_cnt
    for island in range(island_cnt):
        for x, y in island_group[island]:
            for dx, dy in steps:
                nx, ny = x + dx, y + dy
                # 다리 건설가능한 후보의 경우
                if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == 0:
                    flag = 0
                    d = 1
                    while 1:
                        nx += dx
                        ny += dy
                        if not (0 <= nx < N and 0 <= ny < M):
                            break
                        # 다리 건설 가능한 경우
                        if Map[nx][ny] != 0:
                            flag = 1
                            break
                        d += 1
                    # 다리 건설가능하고 거리 2이상 + 한번 연결된 적있는 섬이 아닌 경우
                    if flag and d >= 2 and Map[nx][ny] not in graph[Map[x][y]]:
                        temp = deepcopy(graph)
                        temp[Map[x][y]].append(Map[nx][ny])
                        temp[Map[nx][ny]].append(Map[x][y])
                        connect_dfs(Map[nx][ny], temp, connect + [(x,y,nx,ny)])
                        # 지금 섬에서 연결을 여러개 하는 경우 생각을 못함

                        # 다리 연결 풀기
                        tx, ty = x + dx, y + dy



start_x, start_y = -1, -1
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
island_cnt = 1
island_group = []
visit = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visit[i][j] == 0 and Map[i][j] != 0:
            if start_x == -1:
                start_x, start_y = i, j
            visit[i][j] = 1
            Map[i][j] = island_cnt
            group = [(i, j)]
            island_number(i, j)
            island_cnt += 1
            island_group.append(group)
island_cnt -= 1
res = int(1e10)
connect_dfs(1, defaultdict(list), [])
if res != int(1e10):
    print(res)
else:
    print(-1)


