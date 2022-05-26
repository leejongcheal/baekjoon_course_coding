N, K = map(int, input().split())
h, m, s = 0, 0, 0
res = 0
K = str(K)
if K != '0':
    while h <= N:
        if K in str(h)+str(m)+str(s):
            res += 1
        s += 1
        if s == 60:
            m += 1
            s = 0
            if m == 60:
                h += 1
                m = 0
# K 0인경우
else:
    while h <= N:
        if K in str(h)+str(m)+str(s) or s < 10 or m < 10 or h < 10:
            res += 1
        s += 1
        if s == 60:
            m += 1
            s = 0
            if m == 60:
                h += 1
                m = 0
print(res)