def rotate():
    global N,n, L, robot
    robot = [0]+robot[:-1]
    robot[-1] = 0
    L = [L[-1]] + L[0:-1]


def move_robot():
    global N,n, L, robot
    for i in range(n-2,-1,-1):
        if robot[i] == 1:
            if L[i+1] > 0 and robot[i+1] == 0:
                robot[i] = 0
                robot[i+1] = 1
                L[i+1] -= 1
    robot[-1] = 0

def up_robot():
    global N,n, L, robot
    if L[0] > 0:
        L[0] -= 1
        robot[0] = 1


n, K = map(int, input().split())
N = n*2
L = list(map(int, input().split()))
robot = [0]*n
cnt = 0
blank = L.count(0)
while blank < K:
    cnt += 1
    # 회전
    rotate()
    # 로봇 한칸 이동
    move_robot()
    # 로봇 올림
    up_robot()
    blank = L.count(0)
print(cnt)