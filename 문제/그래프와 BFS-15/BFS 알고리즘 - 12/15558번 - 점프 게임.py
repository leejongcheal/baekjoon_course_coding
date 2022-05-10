N, K = map(int, input().split())
L = [list(input()) for _ in range(2)]
q = []
q.append((0, 0))
res = 0
t = 0
# 아 중복방문을 생각못함 ...
while q:
    temp = []
    L[0][t] = L[1][t] = 0
    t += 1
    while q:
        if res:
            break
        x, y = q.pop()
        for nx, ny in [(x, y - 1), (x, y + 1), (x ^ 1, y + K)]:
            if 0 <= ny < N and L[nx][ny] == "1":
                L[nx][ny] = 0  # 방문처리해서 중복방문 못하게
                temp.append((nx, ny))
            elif ny >= N:
                res = 1
                break
    if res:
        break
    q = temp
print(res)
