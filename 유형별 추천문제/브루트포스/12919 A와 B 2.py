from collections import deque, defaultdict
L = input()
target = input()
q = deque()
visit = defaultdict(int)
q.append(target)
res = 0
while q:
    now = q.popleft()
    if len(now) == len(L):
        if now == L:
            res = 1
            break
        continue
    if now[-1] == "A":
        if visit[now[:-1]] == 0:
            visit[now[:-1]] = 1
            q.append(now[:-1])
    if now[0] == "B":
        now = now[1:][::-1]
        if visit[now] == 0:
            visit[now] = 1
            q.append(now)
print(res)