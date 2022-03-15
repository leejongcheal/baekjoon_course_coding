from collections import deque
T = int(input())
t_list = [list(map(int, input()))*2 for _ in range(T)]
K = int(input())
k_list = [tuple(map(int, input().split())) for _ in range(K)]
t_start = [0]*T
for t_index, direction in k_list:
    t_index -= 1
    move_t = [(t_index, direction)]
    visit = [0]*T
    visit[t_index] = 1
    index = 0
    while index < len(move_t):
        now, direction = move_t[index]
        index += 1
        if now - 1 >= 0 and visit[now - 1] == 0:
            visit[now - 1] = 1
            now_start = t_start[now]
            prev_start = t_start[now - 1]
            if t_list[now][now_start:now_start + 8][6] ^ t_list[now - 1][prev_start:prev_start + 8][2] == 1:
                move_t.append((now-1, direction*-1))
        if now + 1 < T and visit[now + 1] == 0:
            visit[now + 1] = 1
            now_start = t_start[now]
            next_start = t_start[now + 1]
            if t_list[now][now_start:now_start + 8][2] ^ t_list[now + 1][next_start:next_start + 8][6] == 1:
                move_t.append((now+1, direction*-1))
    for index, direction in move_t:
        t_start[index] = (t_start[index] - direction) % 8
res = 0
for i in range(T):
    start = t_start[i]
    if t_list[i][start]:
        res += 1
print(res)