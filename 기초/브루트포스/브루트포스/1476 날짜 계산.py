e,s,m = 0,0,0
re, rs, rm = map(int, input().split())
re -= 1
rs -= 1
rm -= 1
i = 1
while not (e == re and s == rs and m == rm):
    i += 1
    e = (e+1) % 15
    s = (s+1) % 28
    m = (m+1) % 19
print(i)