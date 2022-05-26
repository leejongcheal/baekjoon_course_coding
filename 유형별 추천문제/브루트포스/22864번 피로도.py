A, B, C, M = map(int, input().split())
if A > M:
    work = 0
else:
    day = 0
    now_stree, work = 0, 0
    while day < 24:
        day += 1
        if now_stree + A <= M:
            now_stree += A
            work += B
        else:
            now_stree = max(0, now_stree - C)
print(work)