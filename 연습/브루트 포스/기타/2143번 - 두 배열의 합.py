from collections import defaultdict
target = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
sum_cnt = defaultdict(int)
res = 0
for left in range(N):
    now = 0
    for right in range(left, N):
        now += A[right]
        sum_cnt[now] += 1
for left in range(M):
    now = 0
    for right in range(left, M):
        now += B[right]
        res += sum_cnt[target - now]
print(res)