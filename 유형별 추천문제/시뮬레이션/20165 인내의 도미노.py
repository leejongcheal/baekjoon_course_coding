from collections import deque
steps = [(-1, 0),(0, 1),(1, 0),(0, -1)]
dic_str = "NESW"
N, M, R = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
state = [["S"]*M for _ in range(N)]
res = 0
for _ in range(R):
    X, Y, str_d = input().split()
    X = int(X) - 1
    Y = int(Y) - 1
    dx, dy = steps[dic_str.index(str_d)]
    # 무너트리고
    x, y = X, Y
    if state[x][y] == "S":
        state[x][y] = "F"
        res += 1
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()
            for i in range(1, Map[x][y]):
                nx, ny = x + dx*i, y + dy*i
                if 0 <= nx < N and 0 <= ny < M:
                    if state[nx][ny] == "S":
                        state[nx][ny] = "F"
                        res += 1
                        q.append((nx, ny))
    # 수비자 세움
    x, y = map(int, input().split())
    state[x-1][y-1] = "S"
print(res)
for s in state:
    print(" ".join(s))