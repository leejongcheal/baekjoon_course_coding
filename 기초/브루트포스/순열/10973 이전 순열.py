n = int(input())
find = list(map(int, input().split()))
res = [-1]
if find != list(range(1, n + 1)):
    for i in range(n - 2, -1, -1):
        if find[i] > find[i + 1]:
            for j in range(n - 1, i, -1):
                if find[i] > find[j]:
                    find[i], find[j] = find[j], find[i]
                    res = find[:i + 1] + sorted(find[i + 1:], reverse=True)
                    break
            break
print(" ".join(map(str, res)))