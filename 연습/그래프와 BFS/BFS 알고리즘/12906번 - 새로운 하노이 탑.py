from collections import deque
top = ["A", "B", "C"]
L = []
for i in range(3):
    s = list(input().split())
    if len(s) == 2:
        a = list(s[1])
        while a and a[0] == top[i]:
            a = a[1:]
        L.append(a)
    else:
        L.append([])
q = deque()
visit = []
visit.append(L)
q.append((L, 0))
res = -1
while q:
    L, cnt = q.popleft()
    if len(L[0]) == len(L[1]) == len(L[2]) == 0:
        res = cnt
        break
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if L[i]:
                temp_i = L[i][:-1]
                temp_j = L[j] + [L[i][-1]]
                if temp_j[0] == top[j]:
                    temp_j = temp_j[1:]
                if i == 0 and j == 1:
                    Lij = [temp_i, temp_j, L[2]]
                elif i == 1 and j == 0:
                    Lij = [temp_j, temp_i, L[2]]
                elif i == 0 and j == 2:
                    Lij = [temp_i, L[1], temp_j]
                elif i == 2 and j == 0:
                    Lij = [temp_j, L[1], temp_i]
                elif i == 1 and j == 2:
                    Lij = [L[0], temp_i, temp_j]
                elif i == 2 and j == 1:
                    Lij = [L[0], temp_j, temp_i]
                if Lij not in visit:
                    visit.append(Lij)
                    q.append((Lij, cnt + 1))
print(res)