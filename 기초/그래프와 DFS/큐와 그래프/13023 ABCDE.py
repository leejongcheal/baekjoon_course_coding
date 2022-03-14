from collections import defaultdict
# def dfs(index, cnt, q):
#     global visit, graph
#     print(index, cnt, q)
#     if cnt >= 5:
#         return 1
#     for next in graph[index]:
#         if visit[next] == 0:
#             visit[next] = 1
#             a = dfs(next, cnt + 1, q + [next])
#             visit[next] = 0
#             if a:
#                 return 1
#     return 0
def dfs(index, cnt):
    global visit, graph
    if cnt >= 5:
        return 1
    for next in graph[index]:
        if visit[next] == 0:
            visit[next] = 1
            a = dfs(next, cnt + 1)
            visit[next] = 0
            if a:
                return 1
    return 0


graph = defaultdict(list)
N, M = map(int, input().split())
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
flag = 0
visit = [0]*N
for i in range(N):
    if flag:
        break
    visit[i] = 1
    flag = dfs(i, 1)
    visit[i] = 0
print(flag)