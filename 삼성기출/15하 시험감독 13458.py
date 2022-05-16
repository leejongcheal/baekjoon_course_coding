N = int(input())
L = list(map(int, input().split()))
res = []
B, C = map(int, input().split())
for l in L:
    l -= B
    r = 1
    if l > 0:
        r, c = l//C , l%C
        if c != 0:
            r += 1
        r += 1
    res.append(r)
print(sum(res))