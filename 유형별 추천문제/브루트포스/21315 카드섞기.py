from collections import deque
N = int(input())
target = list(map(int, input().split()))
max_k = 0
for i in range(10):
    if N > 2**i:
        max_k = i
q = deque()
start = [i for i in range(1, N+1)]
q.append((start, -1, -1))
while q:
    L, first, second = q.popleft()
    if L == target:
        res = (first, second)
        break
    if first == -1:
        for i in range(max_k+1):
            temp = L[::]
            for level in range(i, -1, -1):
                if level == i:
                    temp = temp[N - 2**level:] + temp[: N - 2**level]
                    continue
                temp = temp[2**level: 2**(level+1)] + temp[:2**level] + temp[2**(level+1):]
            q.append((temp, i, second))
    else:
        for i in range(max_k + 1):
            temp = L[::]
            for level in range(i, -1, -1):
                if level == i:
                    temp = temp[N - 2 ** level:] + temp[: N - 2 ** level]
                    continue
                temp = temp[2 ** level: 2 ** (level + 1)] + temp[:2 ** level] + temp[2 ** (level + 1):]
            q.append((temp, first, i))
print(*res)