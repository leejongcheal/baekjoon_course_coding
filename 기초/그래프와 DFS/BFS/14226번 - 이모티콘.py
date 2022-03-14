from collections import defaultdict
import heapq
S = int(input())
DP = set()
q = [(0, 1, 0)]
while q:
    time, view, temp = heapq.heappop(q)
    if view == S:
        print(time)
        break
    if view - 1 > 0 and (view-1, temp) not in DP:
        DP.add((view-1, temp))
        heapq.heappush(q, (time + 1, view - 1, temp))
    if view + temp <= 1000 and temp == 0 and (view, view) not in DP:
        DP.add((view, view))
        heapq.heappush(q, (time + 1, view, view))
    if view + temp <= 1000 and temp != 0 and (view + temp, temp) not in DP:
        DP.add((view + temp, temp))
        heapq.heappush(q, (time + 1, view + temp, temp))
        if (view + temp,view) not in DP:
            DP.add((view + temp, view))
            heapq.heappush(q, (time + 1, view, view))
