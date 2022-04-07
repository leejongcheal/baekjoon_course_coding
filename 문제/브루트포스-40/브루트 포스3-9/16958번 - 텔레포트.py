import heapq
def solve(a, b):
    DP = [INF]*N
    DP[a] = 0
    q = [(0, a)]
    while q:
        now_dist, now = heapq.heappop(q)
        if now_dist > DP[now]:
            continue
        if now == b:
            return now_dist
        x, y, s = graph[now]
        for next in range(N):
            nx, ny, ns = graph[next]
            dist = abs(x - nx) + abs(y - ny)
            if s == ns == 1 and T < dist:
                dist = T
            if now_dist + dist < DP[next]:
                DP[next] = now_dist + dist
                heapq.heappush(q, (DP[next], next))

INF = int(1e10)
N, T = map(int, input().split())
graph = []
# 다익스트라로 푸는데 텔포의 경우도 생각 거리는 하나하나 다 계산해야하는듯 ㅅㅂ ㅋㅋ
for _ in range(N):
    s, x, y = map(int, input().split())
    graph.append((x,y,s))
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(solve(a - 1, b - 1))
