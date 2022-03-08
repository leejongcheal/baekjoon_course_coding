from itertools import combinations

def cal(A, B):
    global L, n
    sum_A = 0
    for i in A:
        for j in A:
            sum_A += L[i][j]
    sum_B = 0
    for i in B:
        for j in B:
            sum_B += L[i][j]
    return abs(sum_A - sum_B)


n = int(input())
ans = int(1e10)
L = [list(map(int, input().split())) for _ in range(n)]
for cnt in range(1, n//2 + 1):
    for A in list(combinations(range(n), cnt)):
        B = []
        for i in range(n):
            if i not in A:
                B.append(i)
        ans = min(ans, cal(A, B))
print(ans)