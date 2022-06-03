def dfs(L, idx, res):
    if len(L) == 1:
        res = res[:idx] + L[0] + res[idx:]
        print(res)
        return res
    elif len(L) == 0:
        return res
    min_char = min(L)
    min_idx = L.index(min_char)
    res = res[:idx] + min_char + res[idx:]
    print(res)
    res = dfs(L[min_idx+1:], idx+1, res)
    res = dfs(L[:min_idx], idx, res)
    return res
L = list(input())
res = ""
dfs(L, 0, res)
