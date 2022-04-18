e, s, m = map(int, input().split())
e -= 1
s -= 1
m -= 1
# 15 / 28/ 19
p1, p2, p3 = 1,1,1
flag = 1
while flag:
    flag = 0
    val1 = 28*19*p1
    val2 = 15*19*p2
    val3 = 15*28*p3
    if val1 % 15 != 1:
        p1 += 1
        flag = 1
    if val2 % 28 != 1:
        p2 += 1
        flag = 1
    if val3 % 19 != 1:
        p3 += 1
        flag = 1
res = (val1*e + val2*s + val3*m) % (15*28*19)
print(res + 1)