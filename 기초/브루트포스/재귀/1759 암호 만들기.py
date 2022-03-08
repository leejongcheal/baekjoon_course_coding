from itertools import combinations
ans = []
k, n = map(int, input().split())
L = list(input().split())
L.sort()
s = "aeiou"
for candidate in list(combinations(L, k)):
    mo = 0
    for char in candidate:
        if char in s:
            mo += 1
    if mo and len(candidate) - mo >= 2:
        ans.append(candidate)
for r in ans:
    print("".join(r))