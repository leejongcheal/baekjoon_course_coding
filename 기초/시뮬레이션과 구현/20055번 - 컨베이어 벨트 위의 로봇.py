N, K = map(int, input().split())
robot = [0]*2*N
durability = list(map(int, input().split()))
k = durability.count(0)
res = 0
while k < K:
    res += 1
    # 벨트 회전
    temp_robot = [0]*(2*N)
    temp_dur = [0]*(2*N)
    for i in range(2*N):
        temp_robot[(i+1)%(2*N)] = robot[i]
        temp_dur[(i+1)%(2*N)] = durability[i]
    robot = temp_robot
    durability = temp_dur
    robot[N-1] = 0
    # 로봇이동검사
    i = N - 2
    while 0 <= i:
        if durability[i+1] > 0 and robot[i] == 1 and robot[i+1] == 0:
            robot[i] = 0
            robot[i+1] = 1
            durability[i+1] -= 1
        i -= 1
    robot[N - 1] = 0
    if robot[0] == 0 and durability[0] > 0:
        robot[0] = 1
        durability[0] -= 1
    k = durability.count(0)
print(res)
