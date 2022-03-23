from collections import defaultdict, deque
import sys
sys.setrecursionlimit(100000000)
def bfs(L):
    visit = defaultdict(int)
    q = deque()
    visit[(L[0], L[2])] = 1
    q.append((L[0], L[2]))
    while q:
        A, B = q.popleft()
        C = Sum - (A + B)
        if A == B == C:
            return 1
        for x, y in (A, B), (A, C), (B, C):
            if x > y:
                x, y = y, x
            y -= x
            x *= 2
            X = min(x, y, Sum-(x + y))
            Y = max(x, y, Sum-(x + y))
            if visit[(X,Y)] == 0:
                visit[(X, Y)] = 1
                q.append((X, Y))
    return 0


steps = [(0, 1, 2),(0, 2, 1),(1, 2, 0)]
L = list(map(int, input().split()))
Sum = sum(L)
if Sum%3 != 0:
    print(0)
else:
    L.sort()
    if bfs(L):
        print(1)
    else:
        print(0)
