N = int(input())
L = list(map(int, input().split()))
L.sort()
res = 0
if N < 3:
    res = N
else:
    res = 2
    for i in range(2, N):
        for s in range(N-i):
            if L[s] + L[s+1] > L[s+i]:
                res = i + 1
                break
print(res)