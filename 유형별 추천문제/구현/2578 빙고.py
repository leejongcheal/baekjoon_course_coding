def check(Map):
    res = 0
    for m in Map:
        if sum(m) == 0:
            res += 1
    for j in range(5):
        flag = 1
        for i in range(5):
            if Map[i][j] != 0:
                flag = 0
                break
        if flag:
            res += 1
    flag = 1
    for i in range(5):
        if Map[i][i] != 0:
            flag = 0
            break
    if flag:
        res += 1
    flag = 1
    for i,j in [(0, 4),(1, 3),(2,2),(3, 1),(4, 0)]:
        if Map[i][j] != 0:
            flag = 0
            break
    if flag:
        res += 1
    if res >= 3:
        return 1
    else:
        return 0

res = 0
Map = [list(map(int, input().split())) for _ in range(5)]
num_list = []
for _ in range(5):
    num_list += list(map(int, input().split()))
for idx, n in enumerate(num_list):
    for i in range(5):
        for j in range(5):
            if Map[i][j] == n:
                Map[i][j] = 0
    if check(Map):
        res = idx + 1
        break
print(res)