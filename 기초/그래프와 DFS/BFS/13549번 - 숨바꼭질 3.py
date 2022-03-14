from collections import deque, defaultdict
import heapq
# DP = defaultdict(int)
DP = [0]*100001
x, goal = map(int,input().split())
if x > goal:
    print(x - goal)
else:
    q = []
    DP[x] = 1
    heapq.heappush(q,(1, x))
    while q:
        # print(q)
        cnt, x = heapq.heappop(q)
        if x == goal:
            print(DP[x] - 1)
            break
        if x - 1 > 0 and (DP[x-1] == 0 or DP[x-1] > cnt + 1):
            DP[x - 1] = cnt + 1
            heapq.heappush(q,(cnt + 1, x - 1))
        if x + 1 <= 100000 and (DP[x + 1] == 0 or DP[x+1] > cnt + 1):
            DP[x + 1] = cnt + 1
            heapq.heappush(q,(cnt + 1, x + 1))
        if x > 0 and x*2 <= 100000 and (DP[x*2] == 0 or DP[x*2] > cnt):
            DP[x * 2] = cnt
            heapq.heappush(q,(cnt, x * 2))
