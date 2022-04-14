num = \
    [
        ["###", "#.#", "#.#", "#.#", "###"],
        ["..#", "..#", "..#", "..#", "..#"],
        ["###", "..#", "###", "#..", "###"],
        ["###", "..#", "###", "..#", "###"],
        ["#.#", "#.#", "###", "..#", "..#"],
        ["###", "#..", "###", "..#", "###"],
        ["###", "#..", "###", "#.#", "###"],
        ["###", "..#", "..#", "..#", "..#"],
        ["###", "#.#", "###", "#.#", "###"],
        ["###", "#.#", "###", "..#", "###"]
    ]


def dfs(idx, now_sum):
    global res_cnt, res_sum
    if idx == N:
        res_sum += now_sum
        res_cnt += 1
        return
    for num in N_able[idx]:
        dfs(idx + 1, now_sum + num*(10**(N-idx-1)))


N = int(input())
Map = [list(input()) for _ in range(5)]
N_able = []
start_x = 0
for i in range(N):
    able = []
    check_list = []
    for y in range(4*i, 4*i+3):
        for x in range(5):
            if Map[x][y] == "#":
                check_list.append((x, y-4*i))
    for number in range(10):
        check = num[number]
        flag = 0
        for x, y in check_list:
            if check[x][y] == ".":
                flag = 1
                break
        if flag == 0:
            able.append(number)
    N_able.append(able)
if [] in N_able:
    print(-1)
else:
    res = 0
    total = 1
    for i in range(N):
        total *= len(N_able[i])
    for i in range(N):
        res += sum(N_able[i])*(total // len(N_able[i]))*(10**(N-1-i))
        # res += sum(N_able[i])*cnt*(10**(N-1-i))
        # cnt *= len(N_able)
    print(res / total)