H, N = map(int, input().split())
L = list(map(int, input().split()))
res = 0
max_h = max(L)
max_index = L.index(max_h)
li, ri = 0, N-1
left_max, right_max = L[li], L[ri]
while li <= max_index:
    left_max = max(left_max, L[li])
    res += left_max - L[li]
    li += 1
while ri >= max_index:
    right_max = max(right_max, L[ri])
    res += right_max - L[ri]
    ri -= 1
print(res)