def find(a):
    global parent
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    global parent
    A, B = find(a), find(b)
    if A < B:
        parent[A] = B
    else:
        parent[B] = A


N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)
ans = 0
for i in range(1, N + 1):
    if i == parent[i]:
        ans += 1
    # if i == find(i):
    #     ans += 1
print(ans)
