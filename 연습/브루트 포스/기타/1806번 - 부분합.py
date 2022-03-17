N, M = map(int, input().split())
L = list(map(int, input().split()))
res = 0
left = 0
now = 0
for right in range(N):
    now += L[right]
    while now >= M:
        res = min(res, right - left)
        now -= L[left]
        left += 1
print(res)