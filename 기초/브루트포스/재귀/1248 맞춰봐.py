from collections import defaultdict
def check(temp):
    global n, L
    cnt = len(temp)
    for i in range(cnt):
        for j in range(cnt - i):
            val = sum(temp[i:i+j+1])
            if L[i][j] == "+" and val <= 0:
                return 0
            elif L[i][j] == "0" and val != 0:
                return 0
            elif L[i][j] == "-" and val >= 0:
                return 0
    return 1



def dfs(q):
    if len(q) == n:
        return q
    next = len(q)
    ans = 0
    if L[next][0] == "0": #and 0 not in q:
        temp = q + [0]
        if check(temp):
            ans = dfs(q + [0])
    elif L[next][0] == "+":
        for i in range(1, 10):
            # if i not in q:
            temp = q + [i]
            if check(temp):
                ans = dfs(temp)
                if ans:
                    break
    else:
        for i in range(-10, 0):
            # if i not in q:
            temp = q + [i]
            if check(temp):
                ans = dfs(temp)
                if ans:
                    break
    return ans


n = int(input())
s = input()
L = defaultdict(list)
index = 0
ans = []
for i in range(n):
    for j in range(n - i):
        L[i].append(s[index])
        index += 1
visit = [0]*21
if L[0][0] == '0':
    ans = dfs([0])
elif L[0][0] == "+":
    for i in range(1, 11):
        ans = dfs([i])
        if ans:
            break
else:
    for i in range(-10, 0):
        ans = dfs([i])
        if ans:
            break
# print(ans)
# print(L)
print(" ".join(map(str, ans)))