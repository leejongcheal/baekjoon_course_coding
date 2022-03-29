from collections import defaultdict
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
N, M, T = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
r = [list(map(int,input().split())) for _ in range(T)]
total = N*M
for t in range(T):
    m, d, k = r[t]
    if d == 0:
        k *= -1
    c = k % M
    for i in range(m, N + 1, m):
        Map[i - 1] = Map[i-1][c:] + Map[i-1][0:c]
    # 회전 끝
    # for a in Map:
    #     print(a)
    # print()
    adjoin = set()
    for i in range(N):
        for j in range(M):
            if Map[i][j] != 0:
                temp = Map[i][j]
                flag = 0
                for dx, dy in steps:
                    nx, ny = i + dx, j + dy
                    ny = ny % M
                    if 0 <= nx < N and Map[nx][ny] == temp:
                        flag = 1
                        adjoin.add((nx, ny))
                if flag:
                    adjoin.add((i, j))
    total -= len(adjoin)
    for i, j in adjoin:
        Map[i][j] = 0
    if len(adjoin) == 0 and total != 0:
        total_sum = sum([sum(x) for x in Map])
        avc = total_sum / total
        # print(avc, total_sum, total)
        for i in range(N):
            for j in range(M):
                if Map[i][j] != 0:
                    if Map[i][j] < avc:
                        Map[i][j] += 1
                    elif Map[i][j] > avc:
                        Map[i][j] -= 1
    if total == 0:
        break
    # for a in Map:
    #     print(a)
    # print(1)
res = sum([sum(x) for x in Map])
print(res)