from collections import defaultdict
def smell():
    global N, Map, shark_index, K
    for index in shark_index.keys():
        x, y, d= shark_index[index]
        Map[x][y] = [index, K]
def move():
    global N, Map, shark_index, K, shark_d, steps
    temp = defaultdict(int) # index temp임
    pos_index = defaultdict(int) #dict[(x, y)] -> index
    for index in shark_index.keys():
        x, y, d = shark_index[index]
        # 빈칸 찾기
        flag = 0
        """
            nd가 아닌 d로 써놔서 밑에 내냄새 구할때 d가 변해서 shark_d의 잘못된 곳을 가리키게 됨.
            근데 틀렷네?
        """
        for nd in shark_d[(index, d)]:
            dx, dy = steps[nd]
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and Map[nx][ny] == [0,0]:
                if pos_index[(nx, ny)] == 0:
                    pos_index[(nx, ny)] = index
                    temp[index] = (nx ,ny, nd)
                flag = 1
                break
        if flag:
            continue
        # 같은 냄새 칸 찾기
        for nd in shark_d[(index, d)]:
            dx, dy = steps[nd]
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and Map[nx][ny][0] == index and Map[nx][ny][1] > 0:
                if pos_index[(nx, ny)] == 0:
                    pos_index[(nx, ny)] = index
                    temp[index] = (nx ,ny, nd)
                break
    shark_index = temp
def smell_minus():
    global N, Map
    for i in range(N):
        for j in range(N):
            if Map[i][j][1] > 0:
                Map[i][j][1] -= 1
                if Map[i][j][1] == 0:
                    Map[i][j] = [0,0]
steps = [(-1, 0),(1, 0),(0, -1),(0, 1)]
N, M, K = map(int, input().split())
shark_d = defaultdict(list) # dict[(상어번호, d)] -> [1,2,3,4]식
Map = [list(map(int, input().split())) for _ in range(N)]
shark_index = defaultdict() #dict[index] -> x , y , d
now = [] # 상어번호 ,x y sort해서 집어넣기
for i in range(N):
    for j in range(N):
        if Map[i][j] != 0:
            now.append((Map[i][j], i, j))
Map = [[[0,0] for _ in range(N)] for _ in range(N)] # 상어번호 K
now.sort()
D = list(map(int , input().split()))
for index, x, y in now:
    shark_index[index] = (x, y, D[index-1] - 1)
for i in range(1, M+1):
    for j in range(4):
        shark_d[(i, j)] = [x-1 for x in list(map(int ,input().split()))]
cnt = 0
while 1:
    """
        1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력한다.
        1000초까지는 세라는거 임
        cnt >= 1000으로 해서 틀림 굿 
    """
    if cnt >= 1001 or len(shark_index.keys()) == 1:
        break
    cnt += 1
    # 상어 위치에 냄새 뿌리기
    smell()
    # 상어 이동
    move()
    # 냄새 -1
    smell_minus()
if cnt >= 1001:
    cnt = -1
print(cnt)

