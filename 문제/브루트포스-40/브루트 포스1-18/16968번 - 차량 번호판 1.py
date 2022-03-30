L = list(input())
if L[0] == "d":
    cnt = 10
else:
    cnt = 26
for i in range(1, len(L)):
    if L[i] == L[i-1]:
        if L[i] == "c":
            cnt *= 25
        else:
            cnt *= 9
    else:
        if L[i] == "c":
            cnt *= 26
        else:
            cnt *= 10
print(cnt)
