N = int(input())
res = set()
for x in range(N + 1):
    for y in range(N-x+1):
        for z in range(N-x-y+1):
            w = N - (x + y + z)
            val = 1*x + 5*y + 10*z + w*50
            res.add(val)
print(len(res))