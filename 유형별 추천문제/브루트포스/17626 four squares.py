import math
n = int(input())
INF = int(1e10)
DP = [INF]*(n+5)
DP[0] = 0
for i in range(1, int(math.sqrt(n))+1):
    DP[i*i] = 1
for num in range(1, n+1):
    if DP[num] != INF:
        continue
    for i in range(int(math.sqrt(num))+1):
        DP[num] = min(DP[num], DP[i*i] + DP[num - i*i])
print(DP[n])