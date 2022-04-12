from collections import defaultdict
N, K = map(int, input().split())
q = []
visit = set()# t%2, 위치
odd_visit = defaultdict(int)
even_visit = defaultdict(int)
q.append((N))
t = 1
INF = int(1e10)
res = INF
temp_k = K
if N == K:
    res = 0
else:
    while q:
        temp = []
        temp_k += t
        if K > 500000:
            break
        while q:
            x = q.pop()
            for nx in [x-1,x+1,x*2]:
                if 0 <= nx <= 500000:
                    if t%2 == 0 and even_visit[nx] == 0:
                        temp.append(nx)
                        even_visit[nx] = t
                    elif t%2 == 1 and odd_visit[nx] == 0:
                        temp.append(nx)
                        odd_visit[nx] = t
        t += 1
        q = temp
t = 1
# 홀수초내에 방문을 했다는건 예를들어서 최소 3초에 방문했다면 3,5,7,9초도 가능하다는 뜻
while K <= 5000000:
    K += t
    if even_visit[K] != 0 and even_visit[K] <= t and t%2 == 0:
        res = min(res, t)
    if odd_visit[K] != 0 and odd_visit[K] <= t and t%2 == 1:
        # t초 보다작다면 t초에 그값을 만들수 있다는 뜻이므로 t의값을 비교하면됨.
        # 그러나 t초보다 큰값이면 t초에 그그값에 도달할수 없어서 답자체가 안됨.
        res = min(res, t)
    t += 1
if res == INF:
    print(-1)
else:
    print(res)
