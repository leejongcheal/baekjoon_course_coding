from itertools import permutations
def cal(L):
    global n
    val = 0
    for i in range(n - 1):
        val += abs(L[i] - L[i+1])
    return val
n = int(input())
L = list(map(int, input().split()))
ans = -1e10
for perm in list(permutations(L, n)):
    ans = max(ans, cal(perm))
print(ans)