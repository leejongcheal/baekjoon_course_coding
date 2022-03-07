def check(L,x ,y):
    global max_len
    pre = L[0][y]
    length = 0
    for i in range(n):
        if pre == L[i][y]:
            length += 1
            max_len = max(max_len, length)
        else:
            pre = L[i][y]
            length = 1
    pre = L[x][0]
    length = 0
    for j in range(n):
        if pre == L[x][j]:
            length += 1
            max_len = max(max_len, length)
        else:
            pre = L[x][j]
            length = 1


n = int(input())
L = [list(input()) for _ in range(n)]
max_len = 1
for i in range(n):
    pre = L[i][0]
    length = 0
    for j in range(n):
        if pre == L[i][j]:
            length += 1
            max_len = max(max_len, length)
        else:
            pre = L[i][j]
            length = 1
for j in range(n):
    pre = L[0][j]
    length = 0
    for i in range(n):
        if pre == L[i][j]:
            length += 1
            max_len = max(max_len, length)
        else:
            pre = L[i][j]
            length = 1
for i in range(n):
    for j in range(n):
        if j + 1 < n and L[i][j] != L[i][j+1]:
            L[i][j], L[i][j+1] = L[i][j+1], L[i][j]
            check(L,i, j)
            check(L, i, j + 1)
            L[i][j], L[i][j+1] = L[i][j+1], L[i][j]
        if i + 1 < n and L[i][j] != L[i+1][j]:
            L[i][j], L[i + 1][j] = L[i + 1][j], L[i][j]
            check(L, i, j)
            check(L, i + 1, j)
            L[i][j], L[i + 1][j] = L[i + 1][j], L[i][j]
print(max_len)

