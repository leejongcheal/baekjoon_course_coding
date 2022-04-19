from collections import deque, defaultdict
DP = defaultdict(int)
x, goal = map(int,input().split())
q = deque()
DP[x] = 1
q.append(x)
while q:
    x = q.popleft()
    if x == goal:
        print(DP[goal] - 1)
        break
    for next in [x*2, x + 1, x - 1]:
        if 0 <= next <= 100000 and DP[next] == 0:
            DP[next] = DP[x] + 1
            q.append(next)
