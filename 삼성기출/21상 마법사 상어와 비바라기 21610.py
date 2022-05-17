steps = [(0, -1),(-1, -1),(-1, 0),(-1 ,1),(0, 1),(1, 1),(1, 0),(1, -1)]
check_steps = [(-1, -1),(-1, 1),(1, 1),(1, -1)]
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]
rain = [(N-1, 0),(N-1,1),(N-2,0),(N-2, 1)]
for i in range(M):
    d, s = move[i]
    d -= 1
    after_rain = []
    dx, dy = steps[d]
    for rx, ry in rain:
        nrx, nry = (rx+dx*s)%N, (ry + dy*s)%N
        after_rain.append((nrx, nry))
    # 구름 +1 해주고 대각선 확인해야함 순서대로하자
    for rx, ry in after_rain:
        Map[rx][ry] += 1
    # 증가한칸 대각선확인
    for rx, ry in after_rain:
        cnt = 0
        for ddx, ddy in check_steps:
            nrx, nry = rx + ddx, ry + ddy
            if 0 <= nrx < N and 0 <= nry < N and Map[nrx][nry] > 0:
                cnt += 1
        Map[rx][ry] += cnt
    # 다음 구름 찾기
    rain = []
    for i in range(N):
        for j in range(N):
            if Map[i][j] >= 2 and (i, j) not in after_rain:
                rain.append((i, j))
                Map[i][j] -= 2
print(sum([sum(m) for m in Map]))