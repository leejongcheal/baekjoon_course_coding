from collections import defaultdict
N, M = map(int, input().split())
L = sorted([list(input()) for _ in range(N)])
res_s = ""
for j in range(M):
    cnt = defaultdict(int)
    for i in range(N):
        cnt[L[i][j]] += 1
    res = []
    for key in cnt.keys():
        res.append([cnt[key], key])
    res.sort(key=lambda x:((-1*x[0]), x[1]))
    res_s += res[0][1]
res_cnt = 0
for i in range(N):
    for j in range(M):
        if res_s[j] != L[i][j]:
            res_cnt += 1
print(res_s)
print(res_cnt)
