from collections import defaultdict
from itertools import combinations
def check(A):
    L = [A[0]]
    q = [A[0]]
    while q:
        now = q.pop()
        for next in graph[now]:
            if next in A and next not in L:
                L.append(next)
                q.append(next)
    for a in A:
        if a not in L:
            return 0
    return 1

N = int(input())
group = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(1, N + 1):
    cnt, *a = map(int, input().split())
    graph[i].extend(a)
# 가능한 그룹 나누기
INF = int(1e10)
res = INF
L = [i for i in range(1, N + 1)]
total = sum(group)
for cnt in range(1, N//2 + 1):
    for A in combinations(L, cnt):
        B = []
        B_sum = 0
        for i in L:
            if i not in A:
                B.append(i)
                B_sum += group[i - 1]
        # 조사할 필요도 없음
        diff = abs(total - 2*B_sum)
        if diff >= res:
            continue
        # A, B가 그룹으로 가능한지 조사하기
        if check(A) and check(B):
            res = diff
if res == INF:
    print(-1)
else:
    print(res)
