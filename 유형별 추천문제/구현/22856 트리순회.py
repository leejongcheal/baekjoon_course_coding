from collections import defaultdict
N = int(input())
child = defaultdict(list)
parent = defaultdict(int)
for i in range(N):
    now, left, right = map(int, input().split())
    parent[left] = now
    parent[right] = now
    child[now] = [left, right]
for i in range(1, N+1):
    if parent[i] == 0:
        start = i
        break
last = start
while child[last][1] != -1:
    last = child[last][1]
move = 0
visit = defaultdict(int)
index = start
while 1:
    visit[index] = 1
    if child[index][0] != -1 and visit[child[index][0]] == 0:
        index = child[index][0]
    elif child[index][1] != -1 and visit[child[index][1]] == 0:
        index = child[index][1]
    elif index == last:
        break
    elif parent[index] != 0:
        index = parent[index]
    move += 1
print(move)