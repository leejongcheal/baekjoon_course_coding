def check(L):
    length = len(L)
    cnt = L[0]
    for i in range(length - 1):
        cnt += abs(L[i] - L[i+1])
    cnt += L[-1]
    return cnt


N, M = map(int, input().split())
res = 2*N*M
Map = [list(map(int, input().split())) for _ in range(N)]
for m in Map:
    res += check(m)
for j in range(M):
    temp =[]
    for i in range(N):
        temp.append(Map[i][j])
    res += check(temp)
print(res)