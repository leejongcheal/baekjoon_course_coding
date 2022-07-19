def cal(a, oper, b):
    if oper == "+":
        res = int(a) + int(b)
    elif oper == "-":
        res = int(a) - int(b)
    elif oper == "*":
        res = int(a) * int(b)
    return str(res)


def dfs(s, index):
    global max_res
    if len(s) <= index + 1:
        res = eval("".join(s))
        max_res = max(res, max_res)
        return
    now = cal(s[index], s[index + 1], s[index + 2])
    new_s = s[:index] +[now] + s[index + 3:]
    dfs(new_s, index+2)
    dfs(s, index+2)


N = int(input())
s = list(input())
max_res = -int(1e10)
dfs(s, 0)
print(max_res)