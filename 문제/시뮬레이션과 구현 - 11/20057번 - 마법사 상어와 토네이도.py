steps = [(0, -1),(1, 0),(0, 1),(-1, 0)]
def sand_move(x, y, dx, dy):
    # N범위 넘어가는건 Map넣지는 않지만 모래가 없어지는거긴함.
    val = Map[x][y]
    ex, ey = x + dx, y + dy
    if dx != 0:
        step10 = [(dx, 1),(dx, -1)]
        step7 = [(0,1),(0,-1)]
        step5 = [(2*dx, 0)]
        step2 = [(0,2),(0,-2)]
        step1 = [(dx*-1, 1), (dx*-1, -1)]
    elif dy != 0:
        step10 = [(1, dy), (-1, dy)]
        step7 = [(1, 0), (-1, 0)]
        step5 = [(0, 2*dy)]
        step2 = [(2, 0), (-2, 0)]
        step1 = [(1, -1*dy), (-1, -1*dy)]
    step_num = [step10, step7,step5,step2,step1]
    num = [10, 7, 5, 2, 1]
    for i, step in enumerate(step_num):
        n = num[i]
        trash = int(val / 100 * n)
        for dx, dy in step:
            nx, ny =  x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                Map[nx][ny] += trash
            Map[x][y] -= trash
    if 0 <= ex < N and 0 <= ey < N:
        Map[ex][ey] += Map[x][y]
    Map[x][y] = 0

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
first_sand = sum([sum(x) for x in Map])
# 이동 구현
x = y = (N-1) // 2
idx = 1
move = 1
d = 0
Map[x][y] = 0
flag = 0
while flag != 1:
    dx, dy = steps[d]
    for i in range(move):
        x += dx
        y += dy
        # 모래이동
        if Map[x][y] != 0:
            sand_move(x, y, dx, dy)
        idx += 1
        if x == 0 and y == 0:
            flag = 1
            break
    d += 1
    if d == 2:
        move += 1
    elif d == 4:
        move += 1
        d = 0
res = first_sand - sum([sum(x) for x in Map])
print(res)