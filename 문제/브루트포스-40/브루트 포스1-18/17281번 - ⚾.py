from itertools import permutations
from collections import defaultdict


res = 0
N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
for order in permutations(range(2,10), 8):
    order = list(order)
    order.insert(3, 1)
    # print(order)
    inning = 0
    index = 0
    out = 0
    runner = [0, 0, 0]
    score = 0
    while inning < N:
        j = order[index % 9]
        now = L[inning][j - 1]
        if now == 1:
            score += runner[2]
            runner = [1, runner[0], runner[1]]
        elif now == 2:
            score += runner[1] + runner[2]
            runner = [0, 1, runner[0]]
        elif now == 3:
            score += sum(runner)
            runner = [0, 0, 1]
        elif now == 4:
            score += 1 + sum(runner)
            runner = [0, 0, 0]
        elif now == 0:
            out += 1
        if out == 3:
            inning += 1
            out = 0
            runner = [0, 0, 0]
        index += 1
    res = max(res, score)
print(res)
