def dfs(val):
    global n, ans
    if val == n:
        ans += 1
        return
    for i in range(1,4):
        if val + i <= n:
            dfs(val + i)
    return
for t in range(int(input())):
    n = int(input())
    ans = 0
    dfs(0)
    print(ans)


