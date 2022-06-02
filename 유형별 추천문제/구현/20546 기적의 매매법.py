money = int(input())
L = list(map(int, input().split()))
m1, stock1 = money, 0
m2, stock2 = money, 0
for i in range(len(L)):
    if m1 >= L[i]:
        stock1 += m1 // L[i]
        m1 = m1%L[i]
prev = L[0]
high = 0
down = 0
for i in range(1, len(L)):
    if prev < L[i]:
        high += 1
        down = 0
    elif prev > L[i]:
        down += 1
        high = 0
    else:
        high = 0
        down = 0
    if high >= 3:
        m2 += stock2*L[i]
        stock2 = 0
    elif down >= 3:
        stock2 += m2 // L[i]
        m2 = m2 % L[i]
    prev = L[i]
m1 = m1 + stock1*L[-1]
m2 = m2 + stock2*L[-1]
if m1 > m2:
    print("BNP")
elif m1 < m2:
    print("TIMING")
else:
    print("SAMESAME")