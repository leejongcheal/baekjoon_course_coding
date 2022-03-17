N, M = map(int, input().split())
L = list(map(int, input().split()))
i = j = 0
now = L[0]
res = 0
while 1:
    # if i > j:
    #     i == j
    if now < M:
        j += 1
        if j >= N:
            break
        now += L[j]
    elif now == M:
        res += 1
        now -= L[i]
        i += 1
        if i >= N:
            break
    elif now > M:
        now -= L[i]
        i += 1
        if i >= N:
            break
    if i > j:
        j = i
        now = L[j]
print(res)