from collections import defaultdict
steps = [(-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0),(1, -1),(0, -1),(-1, -1)]
N, M, k = map(int, input().split())
fire = defaultdict(list)
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r -= 1
    c -= 1
    fire[(r, c)].append((m,s, d))
for _ in range(k):
    after = defaultdict(list)
    for x, y in fire.keys():
        for m, s, d in fire[(x, y)]:
            dx, dy = steps[d]
            nx, ny = (x + dx*s)%N, (y + dy*s)%N
            after[(nx, ny)].append((m, s, d))
    fire = defaultdict(list)
    for x, y in after.keys():
        if len(after[(x, y)]) == 1:
            fire[(x, y)].append(after[(x, y)][0])
        else:
            sum_m , sum_s = 0, 0
            list_d = []
            cnt = len(after[(x, y)])
            for m, s, d in after[(x, y)]:
                sum_m += m
                sum_s += s
                list_d.append(d)
            avg_m = sum_m // 5
            avg_s = sum_s // cnt
            if avg_m == 0:
                continue
            now_d = [0, 2, 4, 6]
            first = list_d[0]%2
            for d in list_d:
                if first != d%2:
                    now_d = [1, 3, 5, 7]
                    break
            for d in now_d:
                fire[(x, y)].append((avg_m, avg_s, d))
res = 0
for x, y in fire.keys():
    for m, s, d in fire[(x, y)]:
        res += m
print(res)