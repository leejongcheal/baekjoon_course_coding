N, M = map(int ,input().split())
L = [list(map(int, input().split())) for _ in range(N)]
res = 0
for i in range(M-2):
    for j in range(i+1,M-1):
        for z in range(j+1, M):
            now = 0
            for n in range(N):
                now += max(L[n][i],L[n][j],L[n][z])
            res = max(now, res)
print(res)