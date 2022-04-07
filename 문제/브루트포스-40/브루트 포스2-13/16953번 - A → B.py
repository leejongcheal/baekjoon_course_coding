from collections import deque
A, B = map(int, input().split())
res = -1
q = deque()
q.append((1, A))
while q:
    cnt, val = q.popleft()
    val1 = 2*val
    if val1 == B:
        res = cnt + 1
        break
    elif val1 < B:
        q.append((cnt + 1, val1))
    val2 = 10*val + 1
    if val2 == B:
        res = cnt + 1
        break
    elif val2 < B:
        q.append((cnt + 1, val2))
print(res)
