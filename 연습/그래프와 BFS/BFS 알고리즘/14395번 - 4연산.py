from collections import defaultdict,deque
a, b = map(int, input().split())
visit = defaultdict(int)
if b == 0:
    print("-")
elif a == b:
    print(0)
else:
    res = -1
    q = deque()
    q.append((a, ""))
    visit[a] = 1
    while q:
        x, traced = q.popleft()
        if x == b:
            res = traced
            break
        if x > b:
            if visit[1] == 0:
                visit[1] = 1
                q.append((1, traced+"/"))
        else:
            for oper in ["*", "+", "/"]:
                next = eval(str(x) + oper + str(x))
                if visit[next] == 0:
                    visit[next] = 1
                    q.append((next, traced + oper))
    if res == -1:
        print(-1)
    else:
        print("".join(res))