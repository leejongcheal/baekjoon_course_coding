from collections import defaultdict, deque
commend = defaultdict(int)
pic = []
N = int(input())
M = int(input())
L = list(map(int, input().split()))
q = []
for l in L:
    commend[l] += 1
    if l not in q:
        if len(q) < N:
            q.append(l)
            continue
        min_idx = 0
        for i in range(len(q)):
            if commend[q[i]] < commend[q[min_idx]]:
                min_idx = i
        commend[q[min_idx]] = 0
        q = q[:min_idx] + q[min_idx+1:]
        q.append(l)
print(*(sorted(q)))