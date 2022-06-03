N, M = map(int, input().split())
trail = [[0]*20 for _ in range(N)]
for _ in range(M):
    com, *a = map(int, input().split())
    if com == 1:
        trail[a[0]-1][a[1]-1] = 1
    elif com == 2:
        trail[a[0]-1][a[1]-1] = 0
    elif com == 3:
        temp = [0]*20
        t = trail[a[0]-1]
        for i in range(0, 19):
            temp[i+1] = t[i]
        trail[a[0]-1] = temp
    elif com == 4:
        temp = [0] * 20
        t = trail[a[0] - 1]
        for i in range(1, 20):
            temp[i - 1] = t[i]
        trail[a[0] - 1] = temp
res = set()
for t in trail:
    res.add(tuple(t))
print(len(res))