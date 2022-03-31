from copy import deepcopy
def dfs(visit, now_index):
    global res
    if now_index >= M - 1:
        val = 0
        index = 0
        while index < M:
            if visit[index] != 1:
                if index == 0:
                    val = int(number[index])
                else:
                    val = eval(str(val) + oper[index - 1] + number[index])
                index += 1
            else:
                if index == 0:
                    val = eval(number[index] + oper[index] + number[index+1])
                else:
                    sum_n = eval(number[index] + oper[index] + number[index+1])
                    val = eval(str(val) + oper[index - 1] + str(sum_n))
                index += 2
        res = max(res, val)
        return
    # 현재 선택
    visit[now_index], visit[now_index + 1] = 1, 1
    tv = tuple(visit)
    if tv not in visit_set:
        visit_set.add(tv)
        dfs(visit, now_index + 2)
    visit[now_index], visit[now_index + 1] = -1, -1
    # 현재선택안하는 경우
    visit[now_index], visit[now_index + 1] = 0, 0
    tv = tuple(visit)
    if tv not in visit_set:
        visit_set.add(tv)
        dfs(visit, now_index + 2)
    visit[now_index], visit[now_index + 1] = -1, -1
    # 다음값을 넘김
    visit[now_index] = 0
    tv = tuple(visit)
    if tv not in visit_set:
        visit_set.add(tv)
        dfs(visit, now_index + 1)
    visit[now_index] = -1


N = int(input())
L = list(input())
number = [L[i] for i in range(N) if i % 2 == 0]
oper = [L[i] for i in range(N) if i % 2 == 1]
M = len(number)
visit_set = set()
res = -(2**32)
if N == 1:
    res = int(number[0])
else:
    dfs([-1]*M, 0)
print(res)
