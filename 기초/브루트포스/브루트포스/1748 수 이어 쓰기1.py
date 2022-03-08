n = input()
digit = len(n)
ans = 0
for i in range(1, digit):
    ans += i*9*(10**(i-1))
ans += digit*(int(n) - (10**(digit-1)) + 1)
print(ans)