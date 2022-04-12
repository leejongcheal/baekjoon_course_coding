from collections import defaultdict
start, end = map(int, input().split())
count = defaultdict(int)
time = defaultdict(int)
count[start] = 1
time[start] = -1
if start == end:
    print(0)
    print(1)
else:
    res = -1
    cnt = 0
    t = 0
    q = [start]
    while q:
        temp = []
        while q:
            x = q.pop()
            if x == end:
                res = t
                cnt = count[x]
                continue
            elif x < end:
                oper = [x - 1, x + 1, x*2]
            elif x > end:
                oper = [x - 1, x + 1]
            for nx in oper:
                if 0 <= nx <= 100000:
                    if time[nx] == 0:
                        time[nx] = t + 1
                        count[nx] = count[x]
                        temp.append(nx)
                    elif time[nx] == t + 1:
                        count[nx] += count[x]
                    elif time[nx] < t + 1:
                        continue
        if res != -1:
            break
        q = temp
        t += 1
    print(res)
    print(cnt)