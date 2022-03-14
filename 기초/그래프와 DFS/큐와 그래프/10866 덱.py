import sys
from collections import deque
t = int(input())
q = deque()
res = []
L = sys.stdin.read().splitlines()
for idx in range(t):
    a,*b = L[idx].split()
    if "push_front" in a:
        q.appendleft(b[0])
    elif "push_back" in a:
        q.append(b[0])
    elif a == "front":
        res.append(q[0] if q else "-1")
    elif a == "back":
        res.append(q[-1] if q else "-1")
    elif a == "size":
        res.append(str(len(q)))
    elif a == "empty":
        res.append('0' if q else "1")
    elif a == "pop_back":
        res.append(q.pop() if q else "-1")
    elif a == "pop_front":
        res.append(q.popleft() if q else "-1")
print("\n".join(res))