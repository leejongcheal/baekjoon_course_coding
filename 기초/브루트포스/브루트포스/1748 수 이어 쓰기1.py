n = int(input())
temp = n
cnt = 0
while temp:
    temp //= 10
    cnt += 1
ans = 0
if cnt == 1:
    ans = n
else:
    a = 9
    for i in range(cnt - 1):
        ans += a * (i+1)
        a *= 10
    ans += (cnt) * (n - 10**(cnt - 1) + 1)
print(ans)