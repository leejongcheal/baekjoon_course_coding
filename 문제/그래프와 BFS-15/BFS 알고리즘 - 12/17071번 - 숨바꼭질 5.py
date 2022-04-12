N, K = map(int, input().split())
q = []
visit = set()# t, 위치
q.append((N))
t = 1
res = -1
if N == K:
    res = 0
while q:
    if res != -1:
        break
    temp = []
    K += t
    if K > 500000:
        break
    while q:
        if res != -1:
            break
        x = q.pop()
        if x > K:
            oper = [x-1,x+1]
        else:
            oper = [x-1,x+1,x*2]
        for nx in oper:
            if nx == K:
                res = t
                break
            elif 0 <= nx <= 500000 and (t, nx) not in visit:
                visit.add((t, nx))
                temp.append(nx)
    t += 1
    q = temp
print(res)
