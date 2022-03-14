from collections import deque, defaultdict
for t in range(int(input())):
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visit = [-1]*(N + 1)
    flag = 0
    for i in range(1, N + 1):
        if flag:
            break
        if visit[i] == -1:
            q = deque()
            q.append((i, 0))
            while q:
                now, toggle = q.popleft()
                for next in graph[now]:
                    if visit[next] == -1:
                        q.append((next, 1^toggle))
                        visit[next] = 1^toggle
                    elif visit[next] == toggle:
                        flag = 1
                        break
                if flag:
                    break
    if flag:
        print("NO")
    else:
        print("YES")