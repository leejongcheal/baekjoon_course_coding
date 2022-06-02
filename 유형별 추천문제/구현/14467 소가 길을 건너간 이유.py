N = int(input())
index = [-1]*11
res = 0
for _ in range(N):
    num, move = map(int, input().split())
    if index[num] == -1:
        index[num] = move
    else:
        if index[num] != move:
            res += 1
        index[num] = move
print(res)