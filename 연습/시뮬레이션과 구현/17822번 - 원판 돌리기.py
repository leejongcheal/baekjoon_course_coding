from copy import deepcopy
steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M, T = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(T):
    x, d, k = map(int, input().split())
    if d == 0:
        d = -1
    # 회전
    for i in range(N):
        if (i + 1) % x == 0:
            Map[i] = Map[i][(d*k)%M:] + Map[i][:(d*k)%M]
    # 인접하는 값 0으로 채우기
    flag = 0 # 인접한 값이 있는경우 1 주기
    # 업데이트 도중에 Map의 값이 바뀌는 경우를 방지하기위해 현재 Map값을 저장해서 비교에 사용함
    new_Map = deepcopy(Map)
    for x in range(N):
        for y in range(M):
            val = new_Map[x][y]
            if val == 0:
                continue
            for dx, dy in steps:
                nx, ny = x + dx, (y + dy) % M
                if 0 <= nx < N and new_Map[nx][ny] == val:
                    flag = 1
                    Map[nx][ny] = 0
                    Map[x][y] = 0
    # 인접한 값이 없는 경우 평균 구하기
    if flag:
        continue
    cnt, total = 0, 0
    for x in range(N):
        for y in range(M):
            if Map[x][y] != 0:
                cnt += 1
                total += Map[x][y]
    if cnt == 0:
        break
    avc = total / cnt
    # 평균과 비교해서 채우기
    for x in range(N):
        for y in range(M):
            if Map[x][y] != 0:
                if Map[x][y] < avc:
                    Map[x][y] += 1
                elif Map[x][y] > avc:
                    Map[x][y] -= 1
print(sum([sum(x) for x in Map]))



