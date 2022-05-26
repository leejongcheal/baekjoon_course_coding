N = int(input())
res = 0
for i in range(len(str(N))*9, 0, -1):
    now = N - i
    if now > 0 and now + sum(list(map(int, str(now)))) == N:
        res = N - i
        break
print(res)