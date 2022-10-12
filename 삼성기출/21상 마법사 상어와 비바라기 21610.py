steps = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
steps_cloud = [(-1,-1),(-1,1),(1,1),(1,-1)]

def move_cloud():
    global N, M, Map, cnt, move, cloud, steps
    new = []
    d, s = move[cnt]
    dx, dy = steps[d]
    for x, y in cloud:
        nx, ny = x + dx*s, y + dy*s
        nx = nx % N
        ny = ny % N
        new.append((nx, ny))
        Map[nx][ny] += 1
    cloud = new

def plus_cloud():
    global N, M, Map, cnt, move, cloud, steps_cloud
    for x, y in cloud:
        for dx, dy in steps_cloud:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0<= ny < N and Map[nx][ny] > 0:
                Map[x][y] += 1
def new_cloud():
    global N, M, Map, cnt, move, cloud, steps_cloud
    new = []
    for i in range(N):
        for j in range(N):
            if Map[i][j] >= 2 and (i, j) not in cloud:
                Map[i][j] -= 2
                new.append((i,j))
    cloud = new
N, M = map(int, input().split())
Map= []
for _ in range(N):
    Map.append(list(map(int, input().split())))
move = []
for _ in range(M):
    d, s = map(int, input().split())
    move.append((d-1,s))
cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
for cnt in range(M):
    # 이동후 비
    move_cloud()
    # 대각선 복사
    plus_cloud()
    # 새로운 구름 생성
    new_cloud()
res = sum([sum(x) for x in Map])
print(res)