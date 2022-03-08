DP = [0]*12
DP[0] = 1
DP[1] = 1
DP[2] = 2
for i in range(3, 12):
    DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
for t in range(int(input())):
    n = int(input())
    print(DP[n])