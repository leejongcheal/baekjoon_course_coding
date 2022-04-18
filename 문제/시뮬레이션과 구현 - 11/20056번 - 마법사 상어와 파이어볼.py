from collections import defaultdict
steps = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
N, M, K = map(int, input().split())
fire = defaultdict(list) # m s d 기록
for _ in range(M):
    x, y , m, s, d = map(int ,input().split())
    x -= 1
    y -= 1
    fire[(x, y)].append((m,s,d))
for t in range(K):
    next = defaultdict(list)
    for x, y in fire.keys():
        for m, s, d in fire[(x, y)]:
            dx, dy = steps[d]
            nx, ny = (x + dx*s)%N, (y + dy*s)%N
            next[(nx, ny)].append((m, s, d))
    # 이동후 합치고 나누기
    fire = defaultdict(list)
    for x, y in next.keys():
        if len(next[(x, y)]) == 1:
            m, s, d = next[(x, y)][0]
            fire[(x, y)].append((m, s, d))
        else:
            sum_m = 0
            sum_s = 0
            m, s, d = next[(x, y)][0]
            div_d = d%2
            flag = 0
            for m, s, d in next[(x, y)]:
                sum_m += m
                sum_s += s
                if d%2 != div_d:
                    flag = 1
            D = [0,2,4,6]
            if flag == 1:
                D = [1, 3, 5, 7]
            next_s = sum_s // len(next[(x, y)])
            if sum_m // 5 != 0:
                for i in range(4):
                    fire[(x, y)].append((sum_m // 5, next_s, D[i]))
res = 0
for x, y in fire.keys():
    for m, s, d in fire[(x, y)]:
        res += m
print(res)