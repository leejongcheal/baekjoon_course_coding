from collections import deque
N, K = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(2)]
q = deque()
q.append((1, 0, 0))
res = 0
while q:
    t, x, y = q.popleft()
    if y >= N:
        res = 1
        break
    if y - 1 >= 0 and y - 1 > t and L[x][y-1] == 1:
        q.append((t+1,x, y-1))
    if y + 1 >= N:
        res = 1
        break
    elif y + 1 >= 0 and y + 1 > t and L[x][y+1] == 1:
        q.append((t+1,x,y+1))
    if y + k >= N:
        res = 1
    elif 0 <= y + k < N and y + k > t and L[x^1][]


