L = [l for l in range(1, 31)]
for _ in range(28):
    L.remove(int(input()))
print(L[0],L[1],sep="\n")