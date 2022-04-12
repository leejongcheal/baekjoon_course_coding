from collections import deque
N, K = map(int, input().split())
L = [list(input()) for _ in range(2)]
q = deque()
q.append((0, 0, 0))
res = 0
while q:
    t, x, y = q.popleft()
    if y >= N:
        res = 1
        break
    if 0 <= y - 1 < N and y - 1 > t and L[x][y-1] == "1":
        q.append((t+1, x, y-1))
    if y + 1 >= N:
        res = 1
        break
    elif 0 <= y + 1 < N and y + 1 > t and L[x][y+1] == "1":
        q.append((t+1, x ,y+1))
    if y + K >= N:
        res = 1
        break
    elif 0 <= y + K < N and y + K > t and L[x^1][y+K] == "1":
        q.append((t+1, x^1, y + K))
print(res)


