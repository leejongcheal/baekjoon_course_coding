from collections import deque
def rotate(x, d, k, Map):
    global N, M
    if d == 0:
        k = -1*k
    for i in range(x-1, N, x):
        Map[i] = Map[i][k:] + Map[i][0:k]
def dfs(Map):
    global N, M, steps1, steps2
    visit = [[0]*M for _ in range(N)]
    max_size = 1
    for i in range(N):
        for j in range(M):
            if Map[i][j] != 0 and visit[i][j] == 0:
                visit[i][j] = 1
                cnt = 1
                value = Map[i][j]
                q = deque([(i,j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in steps1:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == value and visit[nx][ny] == 0:
                            visit[nx][ny] = 1
                            cnt += 1
                            Map[nx][ny] = 0
                            q.append((nx, ny))
                    for dx, dy in steps2:
                        nx, ny = x + dx, (y + dy) % M
                        if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == value and visit[nx][ny] == 0:
                            visit[nx][ny] = 1
                            cnt += 1
                            Map[nx][ny] = 0
                            q.append((nx, ny))
                if cnt > 1:
                    Map[i][j] = 0
                max_size = max(max_size, cnt)
    return max_size > 1

def avg_cal(Map):
    global N, M
    cnt = 0
    total = sum([sum(x) for x in Map])
    for i in range(N):
        for j in range(M):
            if Map[i][j] != 0:
                cnt += 1
    """
     모든 원판이 0 이 되는 경우를 생각 못함
    """
    if cnt == 0:
        return
    avg = total / cnt
    for i in range(N):
        for j in range(M):
            if Map[i][j] != 0:
                if Map[i][j] > avg:
                    Map[i][j] -= 1
                elif Map[i][j] < avg:
                    Map[i][j] += 1


N, M, T = map(int, input().split())
"""
    N, M 으로 되어 있는데 i N j N 풀이해서 찾는라 고생함
"""
steps1 = [(1, 0),(-1, 0)]
steps2 = [(0, 1),(0, -1)]
Map = [list(map(int, input().split())) for _ in range(N)]
T_list = [list(map(int, input().split())) for _ in range(T)] # x d k
for cnt in range(T):
    x, d, k = T_list[cnt]
    k = k%M
    # 회전하기
    rotate(x, d, k, Map)
    # 인접수 찾기
    flag = dfs(Map)
    # 인접수 없는경우 평균 구하고 -1 +1 해주기
    if flag == 0:
        avg_cal(Map)
print(sum([sum(x) for x in Map]))