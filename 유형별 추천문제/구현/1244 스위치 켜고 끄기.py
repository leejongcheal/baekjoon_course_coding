def man(num):
    for i in range(1, N+1):
        if num*i < N+1:
            switch[num*i] ^= 1
        else:
            break
def woman(num):
    ln, rn = num-1, num+1
    while 1 <= ln and rn < N+1:
        if switch[ln] == switch[rn]:
            ln -= 1
            rn += 1
        else:
            break
    for i in range(ln+1, rn):
        switch[i] ^= 1
N = int(input())
switch = [0] + list(map(int, input().split()))
for _ in range(int(input())):
    sex, num = map(int, input().split())
    if sex == 1:
        man(num)
    else:
        woman(num)
switch = switch[1:]
cnt = len(switch) // 20
for i in range(cnt+1):
    print(*switch[20*i: 20*(i+1)])
