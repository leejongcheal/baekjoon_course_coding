from itertools import permutations
def check(L):
    for i in range(n):
        if sign[i] == "<":
            if L[i] > L[i+1]:
                return 0
        else:
            if L[i] < L[i+1]:
                return 0
    return 1


n = int(input())
sign = list(input().split())
max_val = "0"
min_val = "9999999999999999999999"
for candidate in list(permutations(range(10), n + 1)):
    if check(candidate):
        s = "".join(map(str, candidate))
        max_val = max(max_val, s)
        min_val = min(min_val, s)
print(max_val)
print(min_val)