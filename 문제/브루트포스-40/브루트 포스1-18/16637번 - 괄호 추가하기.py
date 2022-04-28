def dfs(val, op_idx, num):
    global res
    if op_idx == oper_cnt:
        res = max(res, val)
    # 한개 가능
    if op_idx + 1 <= oper_cnt:
        temp = eval(str(val) + oper[op_idx] + num[0])
        dfs(temp, op_idx + 1, num[1:])
    # 두개 가능
    if op_idx + 2 <= oper_cnt:
        temp = eval(str(val) + oper[op_idx] + '(' + num[0] + oper[op_idx + 1] + num[1] + ')')
        dfs(temp, op_idx + 2, num[2:])


N = int(input())
idx = 0
num = []
oper = []
for s in list(input()):
    if idx % 2 == 0:
        num.append(s)
    else:
        oper.append(s)
    idx += 1
num_cnt = len(num)
oper_cnt = len(oper)
res = -(1e10)
if N == 1:
    res = int(num[0])
elif N == 3:
    res = eval(num[0] + oper[0] + num[1])
else:
    dfs(int(num[0]), 0, num[1:])
    dfs(eval(num[0] + oper[0] + num[1]), 1, num[2:])
print(res)