N, M = map(int, input().split())
cnt_st = int(input())
sticker = [list(map(int, input().split())) for _ in range(cnt_st)]
index_area = []
for i in range(cnt_st - 1):
    for j in range(i + 1, cnt_st):
        iarea = sticker[i][0] * sticker[i][1]
        jarea = sticker[j][0] * sticker[j][1]
        a, b = i, j
        if jarea > iarea:
            a, b= b, a
        index_area.append([iarea + jarea, a, b])
index_area.sort()
res = 0
for area, i, j in index_area[::-1]:
    flag = 0
    r1, c1 = sticker[i]
    r2, c2 = sticker[j]
    if r2 < c2:
        r2, c2 = c2, r2
    if N >= r1 and M >= c1:
        a, b = max(N - r1, M), min(N - r1, M)
        if r2 <= a and c2 <= b:
            flag = 1

        a, b = max(N, M - c1), min(N, M - c1)
        if r2 <= a and c2 <= b and M >= c1:
            flag = 1
    if N >= c1 and M >= r1:
        a, b = max(N - c1, M), min(N - c1, M)
        if r2 <= a and c2 <= b:
            flag = 1

        a, b = max(N, M - r1), min(N, M - r1)
        if r2 <= a and c2 <= b:
            flag = 1
    if flag == 1:
        res = area
        break
print(res)