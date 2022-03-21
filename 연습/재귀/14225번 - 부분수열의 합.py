N = int(input())
L = list(map(int, input().split()))
L.sort()
max, ans = sum(L), 1
for i in L:
    if ans < i:
        break
    ans += i
print(ans)