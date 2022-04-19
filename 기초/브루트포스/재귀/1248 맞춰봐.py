from collections import defaultdict
def check(temp):
    global n, L
    cnt = len(temp)
    val = 0
    for i in range(cnt):
        val = 0
        for j in range(i, cnt):
            val += temp[j]
        if val > 10 or val < - 10:
            return 0
        if L[i][cnt-1] == "+" and val <= 0:
            return 0
        elif L[i][cnt - 1] == "0" and val != 0:
            return 0
        elif L[i][cnt - 1] == "-" and val >= 0:
            return 0
    return 1



def dfs(q):
    global ans
    if len(q) == n:
        ans = q
        return
    if ans:
        return
    next = len(q)
    if L[next][next] == "0": #and 0 not in q:
        temp = q + [0]
        if check(temp):
            dfs(temp)
    elif L[next][next] == "+":
        for i in range(1, 11):
            # if i not in q:
            temp = q + [i]
            if check(temp):
                dfs(temp)
                if ans:
                    return
    else:
        for i in range(1, 11):
            # if i not in q:
            temp = q + [-i]
            if check(temp):
                dfs(temp)
                if ans:
                    return
    return


n = int(input())
s = input()
L = [[-1]*n for _ in range(n)]
index = 0
ans = []
for i in range(n):
    for j in range(n):
        if j < i:
            continue
        L[i][j] = s[index]
        index += 1
if L[0][0] == '0':
    dfs([0])
elif L[0][0] == "+":
    for i in range(1, 11):
        dfs([i])
else:
    for i in range(1, 11):
        dfs([-i])
print(" ".join(map(str, ans)))