N, M = map(int, input().split())
L = list(map(int, input().split()))
res = -1
for x in range(len(L)-2):
    for y in range(x+1, len(L)-1):
        for z in range(y+1, len(L)):
            now = L[x] + L[y] + L[z]
            if now <= M:
                res = max(now, res)
print(res)