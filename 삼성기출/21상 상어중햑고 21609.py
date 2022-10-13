from collections import defaultdict, deque

def find_block():
    global N, Map, res, M, steps, cand
    visit = [[0]*N for _ in range(N)]
    max_size = 0
    cand = []
    for i in range(N):
        for j in range(N):
            # print(i,j)
            if 1 <= Map[i][j] <= M and visit[i][j] == 0:
                now =[(i, j)]
                visit[i][j] = 1
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in steps:
                        nx, ny = x +dx, y + dy
                        if 0<=nx<N and 0<= ny <N:
                            if (Map[nx][ny] == 0 and (nx,ny) not in now) or (Map[nx][ny] == Map[i][j] and visit[nx][ny]==0):
                                q.append((nx, ny))
                                now.append((nx, ny))
                                visit[nx][ny] = 1
                if len(now) < 2:
                    continue
                if len(now) > max_size:
                    cand = [now]
                    max_size = len(now)
                elif len(now) == max_size:
                    cand.append(now)
    if len(cand) == 0:
        return 0
    else:
        return 1
def find_final_block(cand):
    global N, Map, res, M
    rx, ry = MAX_INDEX, MAX_INDEX
    max_cloud_cnt = 0
    r_can = []
    if len(cand) == 1:
        return cand[0]
    for can in cand:
        now_cnt = 0
        flag = 0
        for x, y in sorted(can):
            if Map[x][y] != 0 and flag == 0:
                nx, ny = x, y
                flag = 1
            elif Map[x][y] == 0:
                now_cnt += 1
        if now_cnt > max_cloud_cnt:
            nx, ny = rx, ry
            max_cloud_cnt = now_cnt
            r_can = can
        elif now_cnt == max_cloud_cnt:
            if (nx, ny) < (rx, ry):
                nx, ny = rx, ry
                max_cloud_cnt = now_cnt
                r_can = can
    return r_can

def remove(final_block):
    global N, Map, res, M
    res += len(final_block)**2
    for x, y in final_block:
        Map[x][y] = -2

def rotate_90():
    global N, Map, res, M
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[N-1-j][i] = Map[i][j]
    Map = temp

def gravity():
    global N, Map, res, M
    for i in range(N-2, -1, -1):
        for j in range(N):
            if 0 <= Map[i][j] <= M and Map[i+1][j] == -2:
                cnt = 1
                while i+cnt < N and Map[i+cnt][j] == -2:
                    cnt += 1
                cnt -= 1
                Map[i][j], Map[i+cnt][j] = Map[i+cnt][j], Map[i][j]


steps = [(1,0),(-1,0),(0,1),(0,-1)]
N, M = map(int, input().split())
MAX_INDEX = N*N
Map = [list(map(int, input().split())) for _ in range(N)]
res = 0
while 1:
    cand = []
    # 가장큰블록 찾고 삭제해서 점수 갱신 -> 없으면 0반환
    if not find_block():
        break
    # 후보중 우선순위 높은거 찾고 삭제
    final_block = find_final_block(cand)
    remove(final_block)
    # 중력
    gravity()
    # 90회전
    rotate_90()
    #중력
    gravity()
print(res)