def dfs(x, y, val_sum, cnt):
    global steps, ans, max_val
    if cnt == k:
        ans = max(ans, val_sum)
    if val_sum + max_val * (k - cnt) < ans:
        return
    for i in range(n):
        for j in range(m):
            if (x, y) < (i, j) and visit_check(i, j):
                visit.append((i, j))
                dfs(i, j, val_sum + L[i][j], cnt + 1)
                visit.remove((i, j))


def visit_check(x, y):
    global steps, visit, n , m
    if (x, y) in visit:
        return 0
    for i, j in visit:
        for dx, dy in steps:
            if i + dx == x and j + dy == y:
                return 0
    return 1


# ans = 0
# 정답이 음수의 값이 나오는 경우를 상정하지 못함 ㅋㅋ
ans = -int(1e10)
steps = [(1,0),(0,1),(-1,0),(0,-1)]
n, m, k = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(n)]
max_val = max([max(x) for x in L])
visit = []
for i in range(n):
    for j in range(m):
        visit = [(i,j)]
        dfs(i, j, L[i][j], 1)
print(ans)
