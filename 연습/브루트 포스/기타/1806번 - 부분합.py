INF = int(1e10)
N, M = map(int, input().split())
L = list(map(int, input().split()))
res = INF
left = 0
now = 0
for right in range(N):
    now += L[right]
    while now >= M:
        # print(left, right, now)
        res = min(res, right - left + 1)
        now -= L[left]
        left += 1
if res == INF:
    print(0)
else:
    print(res)