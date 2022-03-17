def cal_dic_value():
    global dic_value, L
    for l in L:
        length = len(l) - 1
        for e in l:
            dic_value[e] += 10 ** length
            length -= 1
    return list(dic_value.values())


N = int(input())
L = list(list(input()) for _ in range(N))
keys = []
for l in L:
    keys += l
keys = set(keys)
dic_value = dict()# 자리수를 계산한값
for key in keys:
    dic_value[key] = 0
value_list = cal_dic_value()
value_list.sort(reverse=True)
res = 0
number = 9
for v in value_list:
    res += number * v
    number -= 1
print(res)
