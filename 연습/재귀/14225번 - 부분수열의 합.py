from itertools import combinations
from collections import defaultdict
N = int(input())
L = list(map(int, input().split()))
num_dict = defaultdict(int)
for i in range(1, N + 1):
    for comb in combinations(L, i):
        num_dict[sum(comb)] += 1
index = 1
while 1:
    if num_dict[index] == 0:
        break
    index += 1
print(index)