N = int(input())
day = 366
schedule = [[0]*day]
h = 1
L = []
for _ in range(N):
    start, end = map(int, input().split())
    L.append((start, end - start))
L.sort(key=lambda x:(x[0], -1*x[1]))
for i in range(N):
    start, minus = L[i]
    end = start + minus
    flag = 0
    for i in range(h):
        ch = 1
        for j in range(start, end + 1):
            if schedule[i][j] == 1:
                ch = 0
                break
        if ch:
            flag = 1
            for j in range(start, end + 1):
                schedule[i][j] = 1
            break
    if flag == 0:
        schedule.append([0]*day)
        h += 1
        for j in range(start, end + 1):
            schedule[-1][j] = 1
res = 0
width, height = 0, 0
for j in range(day):
    flag = 0
    for i in range(h):
        if schedule[i][j] == 1:
            if flag == 0:
                width += 1
                flag = 1
            height = max(height, i+1)
    if flag == 0:
        res += width*height
        width, height = 0, 0
res += width*height
print(res)