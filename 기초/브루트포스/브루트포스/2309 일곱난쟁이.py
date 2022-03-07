L = []
for _ in range(9):
    L.append(int(input()))
L.sort()
sum_L = sum(L[:7])
flag = 0
for i in range(7):
    if sum_L - L[i] + L[7] == 100:
        L[i],L[7] = L[7], L[i]
        break
    if sum_L - L[i] + L[8] == 100:
        L[i], L[8] = L[8], L[i]
        break
if sum(L[:7]) != 100:
    for i in range(6):
        if flag:
            break
        for j in range(i+1,7):
            if sum_L - L[i] - L[j] + L[7] + L[8] == 100:
                L[i], L[j], L[7], L[8] = L[7], L[8], L[i], L[8]
                flag = 1
                break
L = L[:7]
L.sort()
for l in L:
    print(l)