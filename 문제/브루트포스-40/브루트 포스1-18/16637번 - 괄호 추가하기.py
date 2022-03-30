from copy import deepcopy
def dfs(visit, index, visit_index):
    global res, number, oper
    if index >= M - 1:
        temp = ""
        i = 0
        temp_n = []
        temp_o = []
        while i < M:
            if i < M - 1 and visit[i] == visit[i + 1] != 0:
                val = eval(number[i] + oper[i] + number[i+1])
                temp_n.append(str(val))
                if i + 1 < len(oper):
                    temp_o.append(oper[i + 1])
                i += 2
            else:
                if i < M - 1:
                    temp_n.append(number[i])
                    temp_o.append(oper[i])
                else:
                    temp_n.append(number[i])
                i += 1
        val = int(temp_n[0])
        for i in range(len(temp_n)-1):
            val = int(eval(str(val) + temp_o[i] + temp_n[i+1]))
        res = max(res, val)
    for i in range(index, M - 1):
        # 괄호 넣어주는 경우
        visit[i] = visit[i+1] = visit_index
        dfs(visit, i+2, visit_index + 1)
        visit[i] = visit[i+1] = 0
        # 괄호 안치는 경우
        dfs(visit, i + 1, visit_index)


N = int(input())
L = list(input())
number = [L[i] for i in range(N) if i % 2 == 0]
oper = [L[i] for i in range(N) if i % 2 == 1]
M = len(number)
visit = [0]*len(number)
res = 0
if N == 1:
    res = int(number[0])
else:
    dfs(visit, 0, 1)
print(res)