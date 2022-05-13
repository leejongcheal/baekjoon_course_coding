N = int(input())
left = [ (-2, 0, 0.02), (-1, 0, 0.07), (+1, 0, 0.07), (+2, 0, 0.02),(-1, +1, 0.01), (+1, +1, 0.01), (-1, -1, 0.1),
        (+1, -1, 0.1), (0, -2, 0.05)]
down = [(0, -2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02), (-1, -1, 0.01), (-1, 1, 0.01), (1, -1, 0.1),
        (1, 1, 0.1), (2, 0, 0.05)]
right = [(-2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (2, 0, 0.02), (-1, -1, 0.01), (1, -1, 0.01), (-1, 1, 0.1),
         (1, 1, 0.1), (0, 2, 0.05)]
up = [(0, -2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (0, 2, 0.02), (1, -1, 0.01), (1, 1, 0.01), (-1, -1, 0.1),
        (-1, 1, 0.1), (-2, 0, 0.05)]
def move(step, dx, dy, cnt):
    global x, y, flag
    for i in range(cnt):
        x += dx
        y += dy
        original = Map[x][y]
        Map[x][y] = 0
        temp = 0
        for ddx, ddy, ratio in step:
            nx, ny = x + ddx , y + ddy
            temp += int(original*ratio)
            if 0 <= nx < N and 0 <= ny < N:
                Map[nx][ny] += int(original*ratio)
        nx, ny = x +dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            Map[nx][ny] += (original - temp)
        if x == 0 and y == 0:
            flag = 1
            return

Map = [list(map(int, input().split())) for _ in range(N)]
total = sum([sum(x) for x in Map])
x, y = N // 2, N // 2
cnt = 1
flag = 0
while 1:
    # 왼쪽이동
    dx, dy = 0, -1
    move(left,dx, dy,cnt)
    if flag:
        break
    # 아래이동
    dx, dy = 1, 0
    move(down, dx, dy, cnt)
    #
    cnt += 1
    # 오른쪽이동
    dx, dy = 0, 1
    move(right, dx, dy, cnt)
    # 위이동
    dx, dy = -1, 0
    move(up, dx, dy, cnt)
    #
    cnt += 1
print(total - sum([sum(x) for x in Map]))