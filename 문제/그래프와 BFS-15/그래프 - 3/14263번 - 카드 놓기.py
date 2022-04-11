from collections import deque, defaultdict
import heapq


def find(val):
    L = []
    for i in range(N):
        for j in range(M):
            if Map[i][j] == val:
                L.append([i, j])
    L.sort()
    n_list = [i for i in range(L[0][0], L[-1][0] + 1)]
    L.sort(key=lambda x: x[1])
    m_list = [i for i in range(L[0][1], L[-1][1] + 1)]
    group = set()
    for i in n_list:
        for j in m_list:
            group.add((i, j))
    return group


steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]
groups = defaultdict(set)
for i in range(N):
    for j in range(M):
        if Map[i][j]!= "." and Map[i][j] not in groups.keys():
            groups[Map[i][j]] = find(Map[i][j])
indegree = defaultdict(int)
graph = defaultdict(list)
visit = []
flag = 0
for i in range(N):
    for j in range(M):
        if flag:
            # 존재하지 않는 경우
            break
        if Map[i][j] != ".":
            for dx, dy in steps:
                ni, nj = i + dx, j + dy
                if 0 <= ni < N and 0 <= nj < M and Map[ni][nj] not in [".", Map[i][j]] and [Map[i][j], Map[ni][nj]] not in visit:
                    visit.append([Map[i][j], Map[ni][nj]])
                    visit.append([Map[ni][nj], Map[i][j]])
                    inject = groups[Map[i][j]] & groups[Map[ni][nj]]
                    a = 0
                    for x, y in inject:
                        if a == 0 and Map[x][y] in [Map[i][j], Map[ni][nj]]:
                            a = Map[x][y]
                            if a != Map[i][j]:
                                b = Map[i][j]
                            else:
                                b = Map[ni][nj]
                        elif a != 0:
                            if Map[x][y] == b:
                                flag = 1
                                break
                    # 선후 관계 찾은경우
                    if a != 0:
                        if a != Map[i][j]:
                            b = Map[i][j]
                        else:
                            b = Map[ni][nj]
                        graph[b].append(a)
                        indegree[a] += 1

if flag:
    print(-1)
else:
    q = []
    res = ""
    for key in groups.keys():
        if indegree[key] == 0:
            heapq.heappush(q,key)
    while q:
        now = heapq.heappop(q)
        res += now
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                heapq.heappush(q, next)
    print(res)

