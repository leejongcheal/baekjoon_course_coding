import math
def find_prime(N):
    prime = [0]*(N+1)
    prime[1] = 1
    L = []
    for i in range(2, int(math.sqrt(N))+1):
        if prime[i] == 0:
            index = i*2
            while index <= N:
                prime[index] = 1
                index += i
    for i in range(1, N+1):
        if prime[i] == 0:
            L.append(i)
    return L


INF = int(1e10)
N = int(input())
prime = find_prime(N)
res = 0
left = right = 0
now = 0
for right in range(len(prime)):
    now += prime[right]
    while now >= N:
        if now == N:
            res += 1
        now -= prime[left]
        left += 1
print(res)