from collections import deque, defaultdict
x, target = map(int, input().split())
if x == target:
    print(0)
elif target == 0:
    print("-")
else:
    q = deque()
    visit = defaultdict(int)
    q.append((x, ""))
    visit[x] = 1
    res = -1
    while q:
        now, traced = q.popleft()
        if now == target:
            res = traced
            break
        elif now > target:
            next = 1
            if visit[next] == 0:
                visit[next] = 1
                q.append((next, traced + "/"))
        else:
            next = now*now
            if visit[next] == 0:
                visit[next] = 1
                q.append((next, traced + "*"))
            next = now + now
            if visit[next] == 0:
                visit[next] = 1
                q.append((next, traced + "+"))
            next = 1
            if visit[next] == 0:
                visit[next] = 1
                q.append((next, traced + "/"))
    if res != -1:
        print(res)
    else:
        print(-1)