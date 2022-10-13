from collections import defaultdict
def find(s):
    global N, Map, student, res
    for i in range(N):
        for j in range(N):
            if Map[i][j] != 0:
                continue
            love, blank = 0,0
            for dx, dy in steps:
                nx, ny = i +dx, j + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if Map[nx][ny] in student[s]:
                        love += 1
                    elif Map[nx][ny] == 0:
                        blank += 1
                if (love, blank, -1*i, -1*j) > res:
                    res = (love, blank, -1*i, -1*j)
    return res

def cal_res():
    global N, Map, student, res
    for i in range(N):
        for j in range(N):
            love = 0
            s = Map[i][j]
            for dx, dy in steps:
                nx, ny = i +dx, j + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if Map[nx][ny] in student[s]:
                        love += 1
            res += int(10**(love-1))
N = int(input())
Map = [[0]*N for _ in range(N)]
student = defaultdict(set)
steps = [(1, 0),(-1, 0),(0, 1),(0, -1)]
for _ in range(N*N):
    a, *b = map(int, input().split())
    student[a] = set(b)
for s in student.keys():
    res = (-1, -1, -1*N, -1*N)
    find(s)
    x, y = -1*res[2], -1*res[3]
    Map[x][y] = s
res = 0
cal_res()
print(res)