from collections import deque
steps = [(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]
for _ in range(int(input())):
    N = int(input())
    x, y = map(int, input().split())
    visit = [[0]*N for _ in range(N)]
    goal_x, goal_y = map(int, input().split())
    q = deque()
    q.append((x, y, 0))
    time = 0
    while q:
        x, y, t = q.popleft()
        if x == goal_x and y == goal_y:
            time = t
            break
        for dx, dy in steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:

                visit[nx][ny] = 1
                q.append((nx,ny,t + 1))
    print(time)