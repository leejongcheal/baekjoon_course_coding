from collections import deque
from itertools import combinations
steps = [(0, 1),(0, -1),(-1, 0)]
def solve(enemy_pos, cnt, Map):
    global res
    r = 0
    while cnt:
        attack = set()
        # 궁수공격
        for a in archer:
            now_res = D
            now = []
            q = deque()
            q.append((N-1, a, 1))
            while q:
                x, y, dist = q.popleft()
                if dist > now_res:
                    break
                if Map[x][y] == 1:
                    now_res = dist
                    now.append([x, y])
                for dx, dy in steps:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        q.append((nx, ny, dist + 1))
            if now:
                now.sort(key=lambda x:x[1])
                attack.add(tuple(now[0]))
        # 적 업데이트
        r += len(attack)
        for x, y in attack:
            enemy_pos.remove([x, y])
            Map[x][y] = 0
        # 적 내려가기
        new_enemy = []
        for x, y in enemy_pos:
            Map[x][y] = 0
            x += 1
            if x == N:
                continue
            new_enemy.append([x, y])
        for x, y in new_enemy:
            Map[x][y] = 1
        enemy_pos = new_enemy
        cnt = len(enemy_pos)
    res = max(res, r)



N, M, D = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(N)]
enemy_pos = []
for i in range(N):
    for j in range(M):
        if origin[i][j] == 1:
            enemy_pos.append([i, j])
enemy_total = len(enemy_pos)
res = 0
for archer in combinations(range(M), 3):
    temp = [origin[i][:] for i in range(N)]
    solve(enemy_pos[:], enemy_total, temp)
print(res)