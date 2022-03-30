a, b, c, x, y = map(int, input().split())
temp = 0
if a + b > 2*c:
    if x <= y:
        temp = 2*c*x
        if 2*c < b:
            temp += 2*c*(y - x)
        else:
            temp += (y - x)*b
    else:
        temp = 2*c*y
        if 2*c < a:
            temp += 2*c*(x - y)
        else:
            temp += (x - y)*a
else:
    temp = a*x + b*y
print(temp)