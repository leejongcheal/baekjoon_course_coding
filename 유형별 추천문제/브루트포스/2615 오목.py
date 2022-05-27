from collections import deque, defaultdict
L = [list(map(int, input().split())) for _ in range(19)]
steps = [(-1, 1),(0, 1),(1, 1),(1, 0)]
res = 0
for i in range(19):
    for j in range(19):
        if L[i][j] != 0:
            q = deque()  # x y d cnt val
            for d in range(len(steps)):
                    q.append((i, j, d, 1, L[i][j]))
            while q:
                x, y, d, cnt, val = q.popleft()
                dx, dy = steps[d]
                nx, ny = x + dx, y + dy
                px, py = i - dx, j - dy
                if cnt == 5:
                    if (not (0 <= nx < 19 and 0 <= ny < 19) or L[nx][ny] != val) and (not (0 <= px < 19 and 0 <= py < 19) or L[px][py] != val):
                        res = (i, j)
                        break
                    else:
                        continue
                if 0 <= nx < 19 and 0 <= ny < 19 and L[nx][ny] == val:
                    q.append((nx, ny, d, cnt+1, val))
            if res:
                break
    if res:
        break
if res == 0:
    print(res)
else:
    x, y = res
    print(L[x][y])
    print(x+1, y+1)