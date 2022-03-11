from itertools import permutations
n = int(input())
for list in permutations(range(1, n+1), n):
    print(" ".join(map(str, list)))

    # def dfs(cnt, now):
#     global visit, n, L
#     if cnt == n:
#         print(" ".join(map(str, now)))
#         return
#     for i in range(n):
#         if visit[i] == 0:
#             visit[i] = 1
#             dfs(cnt + 1, now + [i+1])
#             visit[i] = 0
# n = int(input())
# L = [i for i in range(1, n + 1)]
# visit = [0]*n
# dfs(0, [])