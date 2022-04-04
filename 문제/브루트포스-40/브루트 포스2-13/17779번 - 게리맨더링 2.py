def solve(x, y, d1, d2):
    # 1번 구하기
    p1 = p2 = p3 = p4 = 0
    for i in range(0, x):
        p1 += sum(Map[i][:y + 1])
    t = 0
    for i in range(x, x + d1):
        p1 += sum(Map[i][:y-t])
        t += 1
    # 3번 구하기
    t = 0
    for i in range(x+d1, x + d1 + d2):
        p3 += sum(Map[i][:y-d1 + t])
        t += 1
    for i in range(x + d1 + d2, N):
        p3 += sum(Map[i][:y-d1+d2])
    # 2번 구하기
    for i in range(x + 1):
        p2 += sum(Map[i][y+1:])
    t = 0
    for i in range(x+1, x + d2 + 1):
        p2 += sum(Map[i][y+2+t:])
        t += 1
    # 4번구하기
    t = 0
    for i in range(x + d2 + 1, x + d1 + d2 + 1):
        p4 += sum(Map[i][y + d2 - t:])
        t += 1
    for i in range(x + d1 + d2 + 1, N):
        p4 += sum(Map[i][y-d1 + d2:])
    p5 = total - (p1 + p2 + p3 + p4)
    return max(p1,p2,p3,p4,p5) - min(p1,p2,p3,p4,p5)

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
total = sum([sum(x) for x in Map])
INF = 1e10
res = INF
# x, y, d1, d2 구하기
for x in range(1, N - 2):
    for y in range(1, N - 2):
        for d1 in range(1, N - 2):
            for d2 in range(1, N - 2):
                if x + d1 + d2 <= N - 1 and 0 <= y - d1 < y + d2 and y + d2 <= N - 1:
                    res = min(res ,solve(x, y, d1, d2))
print(res)
