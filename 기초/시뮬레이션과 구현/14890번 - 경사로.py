N, L = map(int, input().split())
Map = [list(map(int,input().split())) for _ in range(N)]
# 행 검사
res = 0
for i in range(N):
    check = set()
    flag = 1
    for j in range(N - 1):
        if flag == 0:
            break
        diff = abs(Map[i][j] - Map[i][j+1])
        # 크기가 2차이인경우
        if diff > 1:
            flag = 0
            break
        if diff == 1:
            if Map[i][j] > Map[i][j+1]:
                cnt = 0
                for next in range(j+1, N):
                    if next not in check and Map[i][next] == Map[i][j+1]:
                        check.add(next)
                        cnt += 1
                        if cnt == L:
                            break
                    else:
                        flag = 0
                        break
                if cnt < L:
                    flag = 0
                    break
            elif Map[i][j] < Map[i][j+1]:
                cnt = 0
                for prev in range(j, -1, -1):
                    if prev not in check and Map[i][prev] == Map[i][j]:
                        check.add(prev)
                        cnt += 1
                        if cnt == L:
                            break
                    else:
                        flag = 0
                        break
                if cnt < L:
                    flag = 0
                    break
    if flag:
        # print(i)
        res += 1
# 열검사
# print("행")
for j in range(N):
    check = set()
    flag = 1
    for i in range(N - 1):
        if flag == 0:
            break
        diff = abs(Map[i][j] - Map[i + 1][j])
        # 크기가 2차이인경우
        if diff > 1:
            flag = 0
            break
        if diff == 1:
            if Map[i][j] > Map[i + 1][j]:
                cnt = 0
                for next in range(i + 1, N):
                    if next not in check and Map[next][j] == Map[i + 1][j]:
                        check.add(next)
                        cnt += 1
                        if cnt == L:
                            break
                    else:
                        flag = 0
                        break
                if cnt < L:
                    flag = 0
                    break
            elif Map[i][j] < Map[i + 1][j]:
                cnt = 0
                for prev in range(i, -1, -1):
                    if prev not in check and Map[prev][j] == Map[i][j]:
                        check.add(prev)
                        cnt += 1
                        if cnt == L:
                            break
                    else:
                        flag = 0
                        break
                if cnt < L:
                    flag = 0
                    break
    if flag:
        # print(j)
        res += 1
print(res)