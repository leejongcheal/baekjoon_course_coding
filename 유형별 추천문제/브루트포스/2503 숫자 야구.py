L = []
for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            continue
        for z in range(1, 10):
            if j == z or z == i:
                continue
            L.append([str(i), str(j), str(z)])
N = int(input())
for _ in range(N):
    num, s, b = input().split()
    num = list(num)
    s, b = int(s), int(b)
    temp = []
    for l in L:
        ts, tb = 0, 0
        for idx, ll in enumerate(l):
            if l[idx] == num[idx]:
                ts += 1
            elif l[idx] in num:
                tb += 1
        if s == ts and b == tb:
            temp.append(l)
    L = temp
print(len(L))