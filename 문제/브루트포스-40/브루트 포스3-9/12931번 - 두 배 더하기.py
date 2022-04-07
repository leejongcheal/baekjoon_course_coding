N = int(input())
A = list(map(int, input().split()))
B = []
for i in A:
    if i != 0:
        B.append(i)
N = len(B)
cnt = 0
while sum(B) != 0:
    flag = 1
    # print(B, cnt)
    for i in range(N):
        if B[i]%2 != 0:
            B[i] -= 1
            cnt += 1
            flag = 0
            continue
    if flag:
        for i in range(N):
            B[i] //= 2
        cnt += 1
print(cnt)
