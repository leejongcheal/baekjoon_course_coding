from collections import deque, defaultdict
DP = defaultdict(int)
x, goal = map(int,input().split())
if x > goal :
    print(x - goal)
else:
    q = deque()
    DP[x] = 0
    q.append(x)
    while q:
        x = q.popleft()
        if x == goal:
            print(DP[x])
            break
        if x - 1 >= 0 and DP[x-1] == 0:
            DP[x - 1] = DP[x] + 1
            q.append(x - 1)
        if x + 1 <= 100000 and DP[x + 1] == 0:
            DP[x + 1] = DP[x] + 1
            q.append(x + 1)
        if x*2 <= 100000 and DP[x*2] == 0:
            DP[x * 2] = DP[x] + 1
            q.append(x*2)