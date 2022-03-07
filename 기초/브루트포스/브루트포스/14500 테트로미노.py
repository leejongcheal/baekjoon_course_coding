# 발상자체가 아주 멋진문제
##   aaa   꼴도 생각을 해야함 ㅋㅋ
##    a   -> 이거 떄문에 dfs포기하고 BFS풀이 했는데 새로운 발상
# 일단 DFS로 푼다음에 ㅗ모양에 대해서만 다시 조사하는 식으로 풀이 발상
# ㅗ모양만 인덱스로 풀든가 두개를 뽑은 상태에서 next가 아닌 now에 대해서 dfs돌리기
# 가지치기 1개를 뽑았을때 val + 3*max(L)이 ans보다 작다면 가지치기 와...
def dfs(x, y, val, cnt):
    global L, ans, N, M, visit, max_val, steps
    if cnt == 4:
        ans = max(ans, val)
        return
    if val + (4- cnt) * max_val < ans:
        return
    for dx, dy in steps:
        nx, ny = x+dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            if cnt == 2:
                dfs(x, y, val+ L[nx][ny], cnt + 1)
            dfs(nx, ny, val + L[nx][ny], cnt + 1)
            visit[nx][ny] = 0


N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
max_val = max([max(l) for l in L])
steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ans = 0
visit = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        dfs(i, j, L[i][j], 1)
        visit[i][j] = 0
print(ans)
