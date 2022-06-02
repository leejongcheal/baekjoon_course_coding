N, M = map(int, input().split())
L = list(map(int, input().split()))
for _ in range(M):
    com, a, b = map(int, input().split())
    if com == 1:
        L[a-1] = b
    elif com == 2:
        for i in range(a-1, b):
            L[i] ^= 1
    elif com == 3:
        for i in range(a-1, b):
            L[i] = 0
    elif com == 4:
        for i in range(a-1, b):
            L[i] = 1
print(*L)