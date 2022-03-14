from collections import defaultdict
import heapq
S = int(input())
DP = [[0]*1001 for _ in range(1001)]
q = [(0, 1, 0)]
while q:
    time, view, temp = heapq.heappop(q)
    if view == S:
        print(time)
        break
    if view - 1 > 0 and DP[view - 1][temp] == 0:
        DP[view - 1][temp] = 1
        heapq.heappush(q, (time + 1, view - 1, temp))
    if view + temp <= 1000 and DP[view][view] == 0 and temp == 0:
        DP[view][view] = 1
        heapq.heappush(q, (time + 1, view, view))
    if view + temp <= 1000 and DP[view + temp][temp] == 0 and temp != 0:
        DP[view + temp][temp] = 1
        heapq.heappush(q, (time + 1, view + temp, temp))
        if DP[view + temp][view] == 0:
            DP[view + temp][view] = 1
            temp = view
            heapq.heappush(q, (time + 1, view, temp))
