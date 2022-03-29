def recursive(N, X):
    if N == 0:
        return 1
    X -= 1
    if X == 0:
        return 0

    temp = X - ham[N - 1]
    if temp == 0:
        return pattie[N - 1]
    elif temp < 0:
        return recursive(N - 1, X)
    elif temp > 0:
        X -= ham[N - 1]

    X -= 1
    if X == 0:
        return 1 + pattie[N-1]

    temp = X - ham[N - 1]
    if temp == 0:
        return 1 + pattie[N - 1]*2
    elif temp < 0:
        return recursive(N - 1, X) + 1 + pattie[N-1]
    elif temp > 0:
        X -= ham[N - 1]

    X -= 1
    if X == 0:
        return 1 + 2*pattie[N-1]



pattie = [0]*51
ham = [0]*51
ham[0] = 1
pattie[0] = 1
for i in range(1, 51):
    ham[i] = 3 + 2*ham[i-1]
    pattie[i] = 1 + 2*pattie[i-1]
index = 0
N, X = map(int, input().split())
res = recursive(N, X)
print(res)