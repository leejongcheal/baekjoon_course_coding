from itertools import combinations
from collections import defaultdict
N, M = map(int, input().split())
L = list(map(int, input().split()))
res = 0
left = L[0:len(L)//2]
right = L[len(L)//2:]
sum_cnt = defaultdict(int)
# M 이 0인경우에 대해서 따로 처리를 해야함
rigth_subgroup = []
for i in range(len(right) + 1):
    rigth_subgroup += list(combinations(right, i))
for group in rigth_subgroup:
    now = 0
    for e in group:
        now += e
    sum_cnt[now] += 1
left_subgroup = []
for i in range(len(left) + 1):
    left_subgroup += list(combinations(left, i))
for group in left_subgroup:
    now = 0
    for e in group:
        now += e
    res += sum_cnt[M-now]
if M == 0 and res != 0:
    res -= 1
print(res)


