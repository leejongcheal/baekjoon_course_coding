from collections import deque, defaultdict
DP = defaultdict(int)
path = defaultdict(int)
start, goal = map(int,input().split())
if start > goal:
    print(start - goal)
    print(" ".join(map(str, [i for i in range(start, goal - 1, -1)])))
else:
    q = deque()
    DP[start] = 0
    q.append(start)
    while q:
        x = q.popleft()
        if x == goal:
            print(DP[x])
            now = x
            ans = []
            while now != start:
                ans.append(now)
                now = path[now]
            ans.append(now)
            print(" ".join(map(str, reversed(ans))))
            break
        if x - 1 >= 0 and DP[x-1] == 0:
            DP[x - 1] = DP[x] + 1
            path[x-1] = x
            q.append(x - 1)
        if x + 1 <= 100000 and DP[x + 1] == 0:
            DP[x + 1] = DP[x] + 1
            path[x + 1] = x
            q.append(x + 1)
        if x*2 <= 100000 and DP[x*2] == 0:
            path[x * 2] = x
            DP[x * 2] = DP[x] + 1
            q.append(x * 2)