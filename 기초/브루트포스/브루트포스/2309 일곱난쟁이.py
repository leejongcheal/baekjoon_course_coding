def dfs(now, list = []):
    if len(list) == 7:
        if sum(list) == 100:
            return list
        else:
            return None
    for i in range(now+1, 9):
        a = dfs(i, list + [L[i]])
        if a:
            return a
    return None

L = []
for _ in range(9):
    L.append(int(input()))
L.sort()
L = dfs(-1)
for l in L:
    print(l)