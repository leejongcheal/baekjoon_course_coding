from collections import deque
A, B, C = map(int, input().split())
A, B, C = sorted((A,B,C))
total = A + B + C
if total % 3 != 0:
    res = 0
else:
    visit = set()
    visit.add((A,B,C))
    q = deque()
    q.append((A,B))
    q.append((B,C))
    q.append((A,C))
    res = 0
    while q:
        a, b = q.popleft()
        c = total - (a + b)
        # print(a, b, c ,a+b+c)
        if a == b == c:
            res = 1
            break
        a, b = a + a, b - a
        if 1 <= a and 1 <= b and 1 <= c:
            t = tuple(sorted((a,b,c)))
            if t not in visit:
                visit.add(t)
                for a, b in [(t[0], t[1]), (t[1], t[2]), (t[0], t[2])]:
                    q.append((a, b))
print(res)