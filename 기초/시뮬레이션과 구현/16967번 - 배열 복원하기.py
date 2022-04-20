def check_A(i, j):
    if 0 <= i < N and 0 <= j < M:
        return 1
    else:
        return 0
def check_B(i, j):
    if 0 +X <= i < N + X and 0 + Y <= j < M + Y:
        return 1
    else:
        return 0

N, M, X, Y = map(int, input().split())
A = [["#"]*M for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N+X)]
cnt = sum([a.count("#") for a in A])
while cnt:
    for i in range(N+X):
        for j in range(M+Y):
            if check_A(i, j) and not check_B(i, j):
                A[i][j] = B[i][j]
            elif check_A(i,j) and check_B(i, j):
                if A[i-X][j-Y] != "#":
                    A[i][j] = B[i][j] - A[i-X][j-Y]
                elif A[i][j] != "#":
                    A[i-X][j-Y] = B[i][j] - A[i][j]
    cnt = sum([a.count("#") for a in A])
for a in A:
    print(*a)