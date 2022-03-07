# 방문한 곳을 visit [i][j] = 1로 두어서 다른 경로로 방문하는건 일단 생략하고 시작해보자
# 아니지 BFS로 방문하면 될꺼같은데? -> 메모리 낭비라도 해서 풀자 -> DFS생각 못하겠어

##   aaa   꼴도 생각을 해야함 ㅋㅋ
##    a
from collections import deque
def bfs(x, y, val ,q):
    global ans,L,N,M,visit
    while q:
        list, val = q.popleft()
        if len(list) == 4:
            if val == 23:
                print(list)
            ans = max(ans, val)
            continue
        for x, y in list:
            for dx, dy in steps:
                nx,ny = x +dx, y + dy
                temp = list + [(nx, ny)]
                temp.sort()
                stemp = tuple(temp)
                if 0 <= nx < N and 0 <= ny < M and (nx,ny) not in list and stemp not in visit:
                    visit.add(stemp)
                    q.append((temp,val + L[nx][ny]))


N , M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
steps = [(1,0),(0,1),(-1,0),(0,-1)]
ans = 0
visit = set()
for i in range(N):
    for j in range(M):
        q = deque()
        q.append(([(i,j)], L[i][j]))
        visit.add((i,j))
        bfs(i, j, L[i][j], q)
print(ans)