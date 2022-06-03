def rotate(r, Map):
    for _ in range(r):
        temp = [m[::] for m in Map]
        for idx, now in enumerate(check):
            for i in range(n):
                nx, ny = check[(idx+1)%4][i]
                x, y = now[i]
                temp[nx][ny] = Map[x][y]
        temp[n//2] = temp[n//2][::-1]
        Map = temp
    return Map


for tc in range(int(input())):
    n, r = map(int, input().split())
    r = (r//45)%8
    check = []
    now = []
    for j in range(n):
        now.append((n//2, j))
    check.append(now)
    now = []
    for i in range(n):
        now.append((i, i))
    check.append(now)
    now = []
    for i in range(n):
        now.append((i, n//2))
    check.append(now)
    now = []
    for i in range(n):
        now.append((i, n-1-i))
    check.append(now)
    Map = [list(map(int, input().split())) for _ in range(n)]
    Map = rotate(r, Map)
    for m in Map:
        print(*m)
