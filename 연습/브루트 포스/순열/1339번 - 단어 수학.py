def cal():
    global keys, dic, L
    res = 0
    for l in L:
        length = len(l) - 1
        val = 0
        for e in l:
            val += dic[e]*(10 ** length)
            length -= 1
        res += val
    return res

def dfs(cnt):
    global res, total, dic, visit
    if cnt == total:
        print(dic)
        res = max(res, cal())
        return
    for key in keys:
        if dic[key] == -1:
            for i in range(9, -1, -1):
                if visit[i] == 0:
                    visit[i] = 1
                    dic[key] = i
                    dfs(cnt + 1)
                    dic[key] = -1
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
for key in keys:
    dic[key] = -1
visit = [0]*10
dfs(0)
print(res)
