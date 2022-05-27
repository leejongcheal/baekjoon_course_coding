N, M = map(int, input().split())
n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]
res = 0
for i in range(n-1):
    for j in range(i+1, n):
        x1, y1 = L[i]
        x2, y2 = L[j]
        if x1*y1 + x2*y2 < res:
            continue
        t1, t2 = max(x2, y2), min(x2, y2)
        con1, con2 = [], []
        if x1 <= N and y1 <= M:
            con1 = [[N, M-y1], [N-x1, M]]
        if x1 <= M and y1 <= N:
            con2 = [[N, M-x1], [N-y1, M]]
        for a, b in con1 + con2:
            if a < 0 or b < 0:
                continue
            if a < b:
                a, b = b, a
            if a >= t1 and b >= t2:
                res = max(res, x1*y1 + x2*y2)
                break
print(res)