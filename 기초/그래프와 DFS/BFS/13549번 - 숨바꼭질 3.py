from collections import deque
DP = [0]*100001
x, goal = map(int,input().split())
if x > goal:
    print(x - goal)
else:
    q = deque()
    DP[x] = 1
    q.append(x)
    while q:
        # print(q)
        x = q.popleft()
        if x == goal:
            print(DP[x] - 1)
            break
        if x > 0 and x*2 <= 100000 and DP[x*2] == 0:
            DP[x * 2] = DP[x]
            q.appendleft(x * 2)
        if x - 1 > 0 and DP[x-1] == 0 :
            DP[x - 1] = DP[x] + 1
            q.append(x - 1)
        if x + 1 <= 100000 and DP[x + 1] == 0 :
            DP[x + 1] = DP[x] + 1
            q.append(x + 1)
