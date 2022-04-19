from collections import deque, defaultdict
DP = defaultdict(int)
x, goal = map(int,input().split())
q = deque()
DP[x] = 0
q.append(x)
while q:
    x = q.popleft()
    if x == goal:
        print(DP[goal])
        break
    for next in [x + 1, x - 1, x*2]:
        if 0 <= next <= 100000 and DP[next] == 0:
            DP[next] = DP[x] + 1
            q.append(next)