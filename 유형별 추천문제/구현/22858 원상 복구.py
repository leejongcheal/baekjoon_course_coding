N, K = map(int , input().split())
L = list(map(int, input().split()))
D = list(map(int, input().split()))
for _ in range(K):
    temp = [0]*N
    for idx, d in enumerate(D):
        temp[d-1] = L[idx]
    L = temp
print(*L)