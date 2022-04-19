from collections import deque, defaultdict
def bfs(now):
    q = deque()
    visit[i] = 1
    q.append(now)
    while q:
        now = q.popleft()
        for next in graph[now]:
            if visit[next] == visit[now]:
                return 1
            elif visit[next] == 0:
                visit[next] = visit[now]%2 + 1
                q.append(next)
    return 0


for tc in range(int(input())):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    visit = [0]*(V + 1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    flag = 0
    for i in range(1, V + 1):
        if visit[i] == 0:
            flag = bfs(i)
        if flag:
            break
    if flag:
        print("NO")
    else:
        print("YES")