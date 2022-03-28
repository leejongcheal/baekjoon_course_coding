from collections import defaultdict, Counter
def spring_summer(Map):
    for key in Map.keys():
        t_list = Map[key]
        i, j = key
        if len(t_list) == 0:
            continue
        new = []
        flag = 0
        trash = []
        for t in t_list:
            if flag:
                trash.append(t)
                continue
            if t <= muck[i][j]:
                muck[i][j] -= t
                t += 1
                if t % 5 == 0:
                    mult_5.append((i, j))
                new.append(t)
            else:
                flag = 1
                trash.append(t)
        Map[key] = new
        for tr in trash:
            muck[i][j] += tr // 2


def fall(Map):
    stesp = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    for x, y in mult_5:
        for dx, dy in stesp:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                Map[(nx, ny)].insert(0,1)


def winter():
    for i in range(N):
        for j in range(N):
            muck[i][j] += A[i][j]



N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
Map = defaultdict(list)
muck = [[5] * N for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    Map[(x,y)].append(z)

for key in Map.keys():
    Map[key].sort()
# for i in range(N):
#     for j in range(N):
#         Map[i][j].sort()
# Map 완성
time = 0
while time < K:
    mult_5 = []  # 나이가 5의 배수인 나무들의 좌표
    # 봄 + 여름
    spring_summer(Map)
    # for m in Map:
    #     print(m)
    # print()
    # for mu in muck:
    #     print(mu)
    # print("봄여름끝")
    # 가을
    fall(Map)
    # for m in Map:
    #     print(m)
    # print()
    # for mu in muck:
    #     print(mu)
    # print("가을끝")
    # 겨울
    winter()
    # for mu in muck:
    #     print(mu)
    # print("겨울울끝")
    time += 1
res = 0
for key in Map.keys():
    res += len(Map[key])
print(res)
