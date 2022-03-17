def cal():
    global keys, dic, L, dic_value
    res = 0
    for l in L:
        length = len(l) - 1
        val = 0
        for e in l:
            decode_val = dic_value[dic[e]]
            if decode_val == -1:
                decode_val = 9
            val += decode_val*(10 ** length)
            length -= 1
        res += val
    return res

def dfs(dic_idx):
    global total, res
    if dic_idx == total:
        res = max(res, cal())
        return
    # 가지치기
    else:
        if res > cal():
            return
    for i in range(9,-1,-1):
        if visit[i] == 0:
            visit[i] = 1
            dic_value[dic_idx] = i
            dfs(dic_idx + 1)
            dic_value[dic_idx] = -1
            visit[i] = 0
N = int(input())
L = list(list(input()) for _ in range(N))
keys = []
for l in L:
    keys += l
keys = set(keys)
total = len(keys)
dic = dict()
res = 0
dic_value = [-1]*(total)
for idx, key in enumerate(keys):
    dic[key] = idx
visit = [0]*10
dfs(0)
print(res)
