def dfs(list, val):
    global Max, visit
    N = len(list)
    if N == 2:
        Max = max(Max, val)
        return
    for i in range(1, N - 1):
        next_l, next_val = list[:i] + list[i+1:], val + list[i-1] * list[i+1]
        tn = tuple(next_l)
        if (tn, next_val) not in visit:
            visit.add((tn, next_val))
            dfs(list[:i] + list[i+1:], val + list[i-1] * list[i+1])


N = int(input())
L = list(map(int, input().split()))
Max = -int(1e10)
visit = set()
dfs(L, 0)
print(Max)
