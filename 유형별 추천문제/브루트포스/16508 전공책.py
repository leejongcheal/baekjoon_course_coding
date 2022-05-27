from itertools import combinations
S = list(input())
n = int(input())
price = []
name = []
for _ in range(n):
    a, b = input().split()
    price.append(int(a))
    name.append(list(b))
res = INF = int(1e10)
for cnt in range(1, n+1):
    for choice in combinations(range(n), cnt):
        choice = list(choice)
        temp = []
        now_price = 0
        for c in choice:
            now_price += price[c]
            temp.append(name[c][::])
        if now_price > res:
            continue
        for s in S:
            find = 0
            for t in temp:
                if s in t:
                    t.remove(s)
                    find = 1
                    break
            if find == 0:
                break
        if find == 0:
            continue
        res = min(res, now_price)
if res == INF:
    res = -1
print(res)