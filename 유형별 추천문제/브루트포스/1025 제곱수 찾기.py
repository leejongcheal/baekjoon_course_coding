from collections import defaultdict
N, M = map(int, input().split())
L = [list(input()) for _ in range(N)]
square = defaultdict(int)
i = 0
res = -1
while i**2 < 10**9:
    square[i**2] = 1
    i += 1
for i in range(N):
    for j in range(M):
        for row_degree in range(-N,N):
            flag = 0
            for col_degree in range(-M,M):
                val = re_val = L[i][j]
                x, y = i, j
                if row_degree == 0 and col_degree == 0:
                    continue
                while 1:
                    nx, ny = x + row_degree, y + col_degree
                    if square[int(val)]:
                        res = max(res, int(val))
                    if square[int(re_val)]:
                        res = max(res, int(re_val))
                    if 0 <= nx < N and 0 <= ny < M:
                        val += L[nx][ny]
                        re_val = L[nx][ny] + re_val
                    else:
                        flag = 1
                        break
                    x, y = nx, ny
            if flag:
                continue
print(res)