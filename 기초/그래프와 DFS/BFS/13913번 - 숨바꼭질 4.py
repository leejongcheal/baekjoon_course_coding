from collections import deque, defaultdict
DP = defaultdict(int)
x, goal = map(int,input().split())
if x > goal:
    print(x - goal)
    print(" ".join(map(str, [i for i in range(x, goal - 1, -1)])))
else:
    q = deque()
    DP[x] = 0
    q.append((x, [x]))
    while q:
        x, tracked = q.popleft()
        if x == goal:
            print(DP[x])
            print(" ".join(map(str, tracked)))
            break
        if x - 1 >= 0 and DP[x-1] == 0:
            DP[x - 1] = DP[x] + 1
            q.append((x - 1, tracked + [x - 1]))
        if x + 1 <= 100000 and DP[x + 1] == 0:
            DP[x + 1] = DP[x] + 1
            q.append((x + 1, tracked + [x + 1]))
        if x*2 <= 100000 and DP[x*2] == 0:
            DP[x * 2] = DP[x] + 1
            q.append((x * 2, tracked + [x * 2]))