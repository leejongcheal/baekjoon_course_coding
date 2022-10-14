from collections import deque, defaultdict

# 못 가는 경우도 생각해야함
def find(x, y):
    global N, fuel, Map
    cand = []
    cand_dist = 10**7
    visit = [[0]*N for _ in range(N)]
    visit[x][y] = 1
    q = deque()
    q.append((x, y, 0))
    while q:
        x, y, dist = q.popleft()
        if dist > cand_dist:
            break
        # 못 가는 경우
        if fuel < dist:
            return -1, -1
        if Map[x][y] >= 2:
            if cand_dist > dist:
                cand.append((x, y))
                cand_dist = dist
                continue
            elif cand_dist == dist:
                cand.append((x, y))
                continue
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and Map[nx][ny] != 1:
                visit[nx][ny] = 1
                q.append((nx, ny, dist + 1))
    # 갈수 없는 경우
    if len(cand) == 0:
        return -1, -1
    fuel -= cand_dist
    cand.sort()
    return cand[0][0], cand[0][1]

def go_target(x, y):
    global N, fuel, Map, now_dist, target
    tx, ty = target[Map[x][y]]
    Map[x][y] = 0
    visit = [[0] * N for _ in range(N)]
    visit[x][y] = 1
    q = deque()
    q.append((x, y, 0))
    while q:
        x, y, dist = q.popleft()
        # 연로 부족으로 못 가는 경우
        if fuel < dist:
            return -1, -1
        if x == tx and y == ty:
            fuel += dist
            return x, y
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and Map[nx][ny] != 1:
                visit[nx][ny] = 1
                q.append((nx, ny, dist + 1))
    # 다 돌았는데 못가는 경우
    return -1, -1
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
N, M, fuel = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
# 0, 1, 2~ 승객번호
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
target = defaultdict(int)
for i in range(M):
    x, y, tx, ty = map(int, input().split())
    Map[x-1][y-1] = i + 2
    target[i+2] = (tx-1, ty-1)
cnt = 0
x, y = sx, sy
while cnt < M:
    cnt += 1
    # 가까운 승객 찾기
    x, y = find(x, y)
    if x == -1 and y == -1:
        fuel = -1
        break
    # target으로 가기
    x, y = go_target(x, y)
    if x == -1 and y == -1:
        fuel = -1
        break
print(fuel)