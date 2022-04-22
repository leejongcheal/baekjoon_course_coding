N, K = map(int, input().split())
inner = list(map(int, input().split()))
robot = [0]*N
time = 0
while inner.count(0) < K:
    time += 1
    # 회전
    inner = [inner[-1]] + inner[:-1]
    robot = [0] + robot[:-2] + [0]
    # 로봇이동
    for i in range(N-2,-1,-1):
        if robot[i] == 1 and robot[i+1] == 0 and inner[i+1] > 0:
            robot[i] = 0
            robot[i+1] = 1
            inner[i+1] -= 1
    robot[-1] = 0
    # 0위치에 로봇올리기
    if inner[0] > 0:
        inner[0] -= 1
        robot[0] = 1
print(time)