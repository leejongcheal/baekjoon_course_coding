a, b, c, d, e, f = map(int, input().split())
for x in range(-999, 1000):
    y = (c+f - (a+d)*x) // (b+e)
    if (c+f - (a+d)*x) % (b+e) == 0:
        if a*x + b*y == c and d*x + e*y == f:
            break
print(x, y)