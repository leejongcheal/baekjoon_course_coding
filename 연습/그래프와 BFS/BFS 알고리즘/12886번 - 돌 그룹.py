from collections import defaultdict, deque

def bfs(L):
    visit = defaultdict(int)
    q = deque()
    visit[(L[0], L[1], L[2])] = 1
    q.append((L[0], L[1], L[2]))
    while q:
        A, B, C = q.popleft()
        if A == B == C:
            return 1
        for x, y in (A, B), (A, C), (B, C):
            if x > y:
                x, y = y, x
            y -= x
            x *= 2
            z = Sum - (x + y)
            temp = tuple(sorted([x, y, z]))
            if visit[temp] == 0:
                visit[temp] = 1
                q.append(temp)
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
