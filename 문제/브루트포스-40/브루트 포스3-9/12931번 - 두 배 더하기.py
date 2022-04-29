N = int(input())
B = list(map(int, input().split()))
N = len(B)
cnt = 0
while sum(B) != 0:
    for i in range(N):
        if B[i]%2 != 0:
            B[i] -= 1
            cnt += 1
    if sum(B) == 0:
        break
    for i in range(N):
        B[i] //= 2
    cnt += 1
print(cnt)
