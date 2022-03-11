from itertools import permutations
n = int(input())
T = tuple(map(int, input().split()))
com_L = list(permutations(range(1, n+1), n))
index = com_L.index(T)
if index == len(com_L) - 1:
    print(-1)
else:
    print(" ".join(map(str, com_L[index + 1])))