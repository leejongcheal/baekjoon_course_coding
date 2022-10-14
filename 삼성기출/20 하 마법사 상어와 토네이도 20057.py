from collections import defaultdict
steps = [(0, -1),(1, 0),(0, 1),(-1, 0)]
next_steps = defaultdict(list)
next_steps[(0, -1)] = next_steps[0] = [
    (0,-2,0.05),(-1,-1,0.1),(1,-1,0.1),(-2,0,0.02),(-1,0,0.07),(1,0,0.07),(2,0,0.02),(-1,1,0.01),(1,1,0.01)
]
next_steps[(1, 0)] = next_steps[1] = [
    (0,-2,0.02),(-1,-1,0.01),(0,-1,0.07),(1,-1,0.1),(2,0,0.05),(-1,1,0.01),(0,1,0.07),(1,1,0.1),(0,2,0.02)
]
next_steps[(0, 1)] = next_steps[2] = [
    (-1,-1,0.01),(1,-1,0.01),(-2,0,0.02),(-1,0,0.07),(1,0,0.07),(2,0,0.02),(-1,1,0.1),(1,1,0.1),(0,2,0.05)
]
"""
ㅋㅋㅋ 2,0,0.05로 두고품 ㅋㅋㅋ 복잡한 인덱스 실수 많이하는거 주의
"""
next_steps[(-1, 0)] = next_steps[3] = [
    (0,-2,0.02),(-1,-1,0.1),(0,-1,0.07),(1,-1,0.01),(-2,0,0.05),(-1,1,0.1),(0,1,0.07),(1,1,0.01),(0,2,0.02)
]
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
x, y = N//2, N//2
res = 0
cnt = 0
flag = 1
total = sum([sum(x) for x in Map])
while flag:
    cnt += 1
    for idx, (dx, dy) in enumerate(steps):
        if idx == 2:
            cnt += 1
        next_step = next_steps[idx]
        for i in range(cnt):
            x += dx
            y += dy
            # print(x, y)
            rest = Map[x][y]
            Map[x][y] = 0
            original = rest
            rx, ry = x + dx, y + dy
            for ddx, ddy, ratio in next_step:
                nx, ny, value = x + ddx, y + ddy, int(original*ratio)
                rest -= value
                if 0 <= nx < N and 0 <= ny < N:
                    Map[nx][ny] += value
                else:
                    res += value
            if 0 <= rx < N and 0 <= ry < N:
                Map[rx][ry] += rest
            else:
                res += rest
            if x == 0 and y == 0:
                flag = 0
                break
        if flag == 0:
            break
print(res)
