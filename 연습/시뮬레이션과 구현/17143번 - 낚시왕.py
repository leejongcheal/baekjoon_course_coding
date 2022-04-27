from collections import defaultdict
steps = [(-1, 0),(1, 0),(0, 1),(0, -1)]
N, M, S = map(int, input().split())
Map = [[0]*M for _ in range(N)]
shark = defaultdict(int)
for _ in range(S):
    x, y, s, d, z = map(int, input().split())
    x, y, d = x - 1, y - 1, d - 1
    Map[x][y] = 1
    if d < 2:
        s %= 2*(N - 1)
    else:
        s %= 2*(M - 1)
    shark[(x, y)] = [d, s, z]
human = -1
res = 0
while human < M-1:
    human += 1
    # 상어잡기
    for i in range(0, N):
        if Map[i][human] == 1:
            res += shark[(i, human)][2]
            Map[i][human] = 0
            # 예외처리를 위해서 굳이 이것도 0으로 표시해줘야함
            shark[(i, human)] = 0
            break
    # 상어이동
    new_shark = defaultdict(int)
    new_Map = [[0]*M for _ in range(N)]
    for x, y in shark.keys():
        # 위에서 지워진 경우 예외처리, Map으로 하지않는 이유는 밑에서 업데이트 하는 과정에 섞일수 있으니
        if shark[(x, y)] == 0:
            continue
        d, s, z = shark[(x, y)]
        nx, ny = x, y
        idx = 0
        while idx < s:
            dx, dy = steps[d]
            while 0 <= nx + dx < N and 0 <= ny + dy < M and idx < s:
                idx += 1
                nx += dx
                ny += dy
            if idx < s:
                if d in [0, 1]:
                    d = d ^ 1
                else:
                    d = (d-2) ^ 1 + 2
        Map[x][y] = 0
        new_Map[nx][ny] = 1
        if new_shark[(nx, ny)] == 0:
            new_shark[(nx, ny)] = [d, s, z]
        else:
            if new_shark[(nx, ny)][2] < z:
                new_shark[(nx, ny)] = [d,s,z]
    shark = new_shark
    Map = new_Map
print(res)