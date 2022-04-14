from collections import deque, defaultdict
INF = int(1e100)
def solve(N):
    visit = defaultdict(int)
    q = deque()
    q.append(1)
    visit[1] = 1
    while q:
        now = q.popleft()
        if now >= INF:
            return "BRAK"
        if now % N == 0:
            return now
        for next in [now*10, now*10+1]:
            if visit[next % N] == 0:
                visit[next % N] = 1
                q.append(next)
    return "BRAK"

for tc in range(int(input())):
    N = int(input())
    res = solve(N)
    print(res)
