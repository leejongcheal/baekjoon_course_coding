def check(l):
    visit = [0]*N
    pre = l[0]
    for i in range(N):
        if pre == l[i]:
            continue
        elif abs(l[i] - pre) == 1:
            if pre < l[i]:
                cnt = 0
                now = i - 1
                flag = 0
                while cnt < L:
                    if 0 <= now < N and l[now] == pre and visit[now] == 0:
                        visit[now] = 1
                        cnt += 1
                        now -= 1
                    else:
                        break
                if cnt != L:
                    return 0
                pre = l[i]
            elif pre > l[i]:
                cnt = 0
                now = i
                flag = 0
                while cnt < L:
                    if 0 <= now < N and l[now] == l[i] and visit[now] == 0:
                        visit[now] = 1
                        cnt += 1
                        now += 1
                    else:
                        break
                if cnt != L:
                    return 0
                pre = l[i]
        else:
            return 0
    return 1


N, L = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
res = 0
for m in Map:
    if check(m):
        res += 1
for j in range(N):
    temp = []
    for i in range(N):
        temp.append(Map[i][j])
    if check(temp):
        res += 1
print(res)









