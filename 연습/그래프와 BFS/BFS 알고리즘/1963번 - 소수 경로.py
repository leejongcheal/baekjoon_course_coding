from collections import deque, defaultdict
prime = defaultdict(int)
for i in range(2, 101):
    index = i
    while index < 10001:
        prime[index] = 1
        index += i
# 소수이면 prime[N] = 0의 값을 가짐
for tc in range(int(input())):
    start, target = map(int, input().split())
    visit = defaultdict(int)
    q = deque()
    # val, cnt 순
    q.append((start, 0))
    visit[start] = 1
    res = -1
    while q:
        now, cnt = q.popleft()
        if now == target:
            res = cnt
            break
        L = []
        # L에 순서반대로 한자리씩 들어감
        for i in range(4):
            now, c = divmod(now, 10)
            L.append(c)
        # 한자리씩 바꾸는 케이스
        for i in range(4):
            for j in range(10):
                if i == 3 and j == 0:
                    continue
                val = 0
                for c in range(4):
                    if c == i:
                        val += j*10**c
                    else:
                        val += L[c]*10**c
                if prime[val] == 0 and visit[val] == 0:
                    visit[val] = 1
                    q.append((val, cnt + 1))
    if res == -1:
        print("Impossible")
    else:
        print(res)