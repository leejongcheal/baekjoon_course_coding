def move(dice, number):
    if number == 1:
        return movedice_1(dice)
    elif number == 2:
        return  movedice_2(dice)
    elif number == 3:
        return  movedice_3(dice)
    elif number == 4:
        return  movedice_4(dice)
def movedice_1(dice):
    temp = [[0], [0, 0, 0], [0], [0]]
    temp[0][0] = dice[0][0]
    temp[1][0], temp[1][1], temp[1][2] = dice[3][0], dice[1][0], dice[1][1]
    temp[2][0] = dice[2][0]
    temp[3][0] = dice[1][2]
    return temp


def movedice_2(dice):
    temp = [[0], [0, 0, 0], [0], [0]]
    temp[0][0] = dice[0][0]
    temp[1][0], temp[1][1], temp[1][2] = dice[1][1], dice[1][2], dice[3][0]
    temp[2][0] = dice[2][0]
    temp[3][0] = dice[1][0]
    return temp


def movedice_3(dice):
    temp = [[0], [0, 0, 0], [0], [0]]
    temp[0][0] = dice[1][1]
    temp[1][0], temp[1][1], temp[1][2] = dice[1][0], dice[2][0], dice[1][2]
    temp[2][0] = dice[3][0]
    temp[3][0] = dice[0][0]
    return temp


def movedice_4(dice):
    temp = [[0], [0, 0, 0], [0], [0]]
    temp[0][0] = dice[3][0]
    temp[1][0], temp[1][1], temp[1][2] = dice[1][0], dice[0][0], dice[1][2]
    temp[2][0] = dice[1][1]
    temp[3][0] = dice[2][0]
    return temp


steps = [(0, 1), (0, -1), (-1, 0), (1, 0)]
N, M, x, y, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
oper_list = list(map(int,input().split()))
dice = [[0], [0, 0, 0], [0], [0]]
for d in oper_list:
    dx, dy = steps[d-1]
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < M:
        dice = move(dice, d)
        if Map[nx][ny] == 0:
            Map[nx][ny] = dice[3][0]
        else:
            dice[3][0] = Map[nx][ny]
            Map[nx][ny] = 0
        print(dice[1][1])
        x, y = nx, ny
