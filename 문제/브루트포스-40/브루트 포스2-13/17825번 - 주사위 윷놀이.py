Map0 = [i for i in range(0, 41, 2)]
Map1 = [10, 13, 16, 19, 25]
Map2 = [20, 22, 24, 25]
Map3 = [30, 28, 27, 26, 25]
Map4 = [25, 30, 35, 40, 41]
Map = [Map0, Map1, Map2, Map3, Map4, [0]]
def move_dice(x, y, num):
    if x == 0: # and Map[x][y] != [10, 20, 30, 25]:
        ny = y + num
        if ny >= len(Map[0]):
            return 5, 0 # 도착
        elif ny == 5:
            return 1, 0
        elif ny == 10:
            return 2, 0
        elif ny == 15:
            return 3, 0
        elif ny == 20:
            return 4, 3
        else:
            return x, ny
    elif x in [1, 2, 3]:
        flag = 0
        for i in range(num):
            y += 1
            if flag == 0 and Map[x][y] == 25:
                x, y = 4, 0
                flag = 1
            elif flag == 1 and Map[x][y] == 41:
                return 5, 0
        return x, y
    elif x == 4:
        for i in range(num):
            y += 1
            if Map[x][y] == 41:
                return 5, 0
        return x, y

def dfs(dice, now, value):
    global res
    # print(now, dice, value, res)
    if now == 10:
        # if sum(value) == 218:
        #     print(dice, value)
        res = max(res, value)
        return
    num = move[now]
    for i, (x, y) in enumerate(dice):
        if x == 5 and y == 0:
            continue
        nx, ny = move_dice(x, y, num)
        if nx == 5 and ny == 0:
            dice[i] = (nx, ny)
            dfs(dice, now + 1, value + Map[nx][ny])
            dice[i] = (x, y)
        elif (nx, ny) not in dice:
            dice[i] = (nx, ny)
            dfs(dice, now + 1, value + Map[nx][ny])
            dice[i] = (x, y)
        elif (nx, ny) in dice:
            continue
    if len(dice) < 10:
        x, y = move_dice(0, 0, num)
        if (x, y) not in dice:
            dfs(dice + [(x, y)], now + 1, value + Map[x][y])


visit = set() # 정렬된 dice을 문자열로 넣어주기
dice = []
move = list(map(int, input().split()))
# 일단 모든 이동에 대해서 검사는 해야함
res = 0
dfs(dice, 0, 0)
print(res)