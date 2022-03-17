H, W, X, Y = map(int, input().split())
Map = [list(map(int,input().split())) for _ in range(H+X)]
temp = [[-1]*W for _ in range(H)]
for i in range(H+X):
    for j in range(W+Y):
        if 0 <= i < X and 0 <= i < H and 0 <= j < W:
            temp[i][j] = Map[i][j]
        elif H <= i and 0 <= i - X < H and 0 <= j - Y < W:
            temp[i-X][j - Y] = Map[i][j]
        elif X <= i < H and 0 <= j < Y:
            temp[i][j] = Map[i][j]
        elif X <= i < H and W <= j < W + Y:
            temp[i - X][j - Y] = Map[i][j]
        elif X <= i < H and Y <= j < W:
            temp[i][j] = Map[i][j] - temp[i-X][j-Y]
for t in temp:
    print(" ".join(map(str, t)))

