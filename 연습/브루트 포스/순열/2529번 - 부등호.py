def dfs(q, reverse_val=0):
    if reverse_val:
        L = group[::-1]
    else:
        L = group
    if len(q) == N + 1:
        return q
    elif len(q) == 0:
        for i in L:
            a = dfs([i], reverse_val)
            if a:
                return a
    sign = sign_list[len(q) - 1]
    for i in L:
        if i not in q:
            a = 0
            if sign == "<" and q[-1] < i:
                a = dfs(q + [i], reverse_val)
            elif sign == ">" and q[-1] > i:
                a = dfs(q + [i], reverse_val)
            if a:
                return a
    return None


N = int(input())
group = [i for i in range(10)]
sign_list = list(input().split())
max_val = dfs([], 1)
min_val = dfs([], 0)
print("".join(map(str, max_val)))
print("".join(map(str, min_val)))