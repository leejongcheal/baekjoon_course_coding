H, W, X, Y = map(int, input().split())
Map = [list(map(int,input().split())) for _ in range(H+X)]
temp = [[-1]*W for _ in range(H)]
for i in range(X):
    for j in range(W):
        temp[i][j] = Map[i][j]
for di in range(X):
    for j in range(W):
        temp[-(di + 1)][j] = Map[-(di + 1)][j+Y]
for i in range(H+X):
    for j in range(W+Y):
        if X <= i < H and 0 <= j < Y:
            temp[i][j] = Map[i][j]
        elif X <= i < H and W <= j < W + Y:
            temp[i - X][j - Y] = Map[i][j]
        elif X <= i < H and Y <= j < W:
            temp[i][j] = Map[i][j] - temp[i-X][j-Y]
for t in temp:
    print(" ".join(map(str, t)))

