A = int(input())
T = int(input())
str = int(input())
i = 0
res = 0
cnt = 0
idx = 0
for i in range(1, 1000):
    now = [0,1,0,1] + [0]*(i+1) + [1]*(i+1)
    for n in now:
        idx += 1
        if n == str:
            cnt += 1
            if cnt == T:
                res = idx
                break
    if res:
        break
print((res-1)%A)