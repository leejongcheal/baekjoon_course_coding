from collections import defaultdict
def find_possible_n(Map, x, y):
    check = defaultdict(int)
    for i in range(9):
        check[Map[x][i]] += 1
        check[Map[i][y]] += 1
    si, sj = (x//3) * 3 ,(y // 3) * 3
    for i in range(3):
        for j in range(3):
            check[Map[si+i][sj+j]] += 1
    L = []
    for i in range(1, 10):
        if check[i] == 0:
            L.append(i)
    return L

def dfs(Map, domino, N):
    steps = [(0, 1), (1, 0)]
    if N == 36:
        return 1
    for i in range(9):
        for j in range(9):
            if Map[i][j] == 0:
                x, y = i, j
                # 오른쪽, 아래로 가는거에서 안채워지는경우에 대한 처리가 안되어 있음
                for dx, dy in steps:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 9 and 0 <= ny < 9 and Map[nx][ny] == 0:
                        for num1 in find_possible_n(Map, x, y):
                            Map[x][y] = num1
                            for num2 in find_possible_n(Map, nx, ny):
                                Map[nx][ny] = num2
                                a, b = num1, num2
                                if a > b:
                                    a, b = b, a
                                if domino[a][b] == 1:
                                    domino[a][b] = 0
                                    print(N)
                                    c = dfs(Map, domino, N+1)
                                    print(1, N, c)
                                    for m in Map:
                                        print(m)
                                    print("domini")
                                    for d in domino:
                                        print(d)
                                    if c:
                                        print(11, a)
                                        return 1
                                    domino[a][b] = 1
                                Map[nx][ny] = 0
                            Map[x][y] = 0
    return 0

tc = 1
while 1:
    N = int(input())
    if N == 0:
        break
    print("Puzzle {}".format(tc))
    tc += 1
    # 도미노 사용 여부
    domino = [[0]*10 for _ in range(10)]
    for i in range(1, 9):
        for j in range(i+1, 10):
            domino[i][j] = 1
    # 맵에 들어간 숫자 관리
    Map = [[0]*9 for _ in range(9)]
    # 도미노 위치 여부
    in_domino = [[0]*9 for _ in range(9)]
    for _ in range(N):
        a, X, b, Y = input().split()
        a = int(a)
        b = int(b)
        x, y = ord(X[0]) - ord("A"), int(X[1]) - 1
        Map[x][y] = a
        x, y = ord(Y[0]) - ord("A"), int(Y[1]) - 1
        Map[x][y] = b
        if b < a:
            a, b = b, a
        domino[a][b] = 1
    L = input().split()
    for i in range(9):
        x, y = ord(L[i][0]) - ord("A"), int(L[i][1]) - 1
        Map[x][y] = i + 1
    # for m in Map:
    #     print(m)
    dfs(Map, domino, N)
    for m in Map:
        print(m)