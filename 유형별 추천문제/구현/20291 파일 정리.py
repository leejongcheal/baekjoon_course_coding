from collections import defaultdict
res = defaultdict(int)
for _ in range(int(input())):
    a, b = input().split(".")
    res[b] += 1
keys = sorted(res.keys())
for key in keys:
    print(key, res[key])