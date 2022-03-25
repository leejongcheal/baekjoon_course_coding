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
        for k in [1, 10, 100, 1000]:
            m_number = now - (now//k) % 10 * k
            for i in range(10):
                val = m_number + i*k
                if prime[val] == 0 and visit[val] == 0 and val >= 1000:
                    visit[val] = 1
                    q.append((val, cnt + 1))
    if res == -1:
        print("Impossible")
    else:
        print(res)