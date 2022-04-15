def find(idx):
    bin_list = []
    for add in addrs:
        val = bin(add[idx])[2:]
        val = "0"*(8-len(val)) + val
        bin_list.append(val)
    flag = 0
    for i in range(8):
        pre = bin_list[0][i]
        for b in bin_list:
            if pre != b[i]:
                flag = 1
                start = i
                break
        if flag == 1:
            break
    start = 8 - start
    res = (1<<start) - 1
    return 255 - res


N = int(input())
networt = []
bitmask = []
addrs = [list(map(int, input().split("."))) for _ in range(N)]
flag = 0
for i in range(4):
    new = 255
    for add in addrs:
        new &= add[i]
    networt.append(new)

flag = 0
for i in range(4):
    if flag == 1:
        bitmask.append(0)
        continue
    for add in addrs:
        if add[i] != networt[i]:
            flag = 1
            val = find(i)
            bitmask.append(val)
            break
    if flag:
        continue
    bitmask.append(255)
bitmask = ".".join(map(str, bitmask))
networt = ".".join(map(str, networt))
print(networt)
print(bitmask)