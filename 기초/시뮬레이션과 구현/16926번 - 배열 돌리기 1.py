def split():
    lines = []
    cnt = min(N, M) // 2
    for level in range(cnt):
        line = []
        x, y = level, level
        line.append(Map[x][y])
        # 밑으로
        while x + 1 < N - level:
            x += 1
            line.append(Map[x][y])
        # 오른쪽으로
        while y + 1 < M - level:
            y += 1
            line.append(Map[x][y])
        # 위로
        while x - 1 >= level:
            x -= 1
            line.append(Map[x][y])
        # 오른쪽으로
        while y - 1 > level:
            y -= 1
            line.append(Map[x][y])
        lines.append(line)
    return lines


def fill(lines):
    cnt = min(N, M) // 2
    for level in range(cnt):
        line = lines[level]
        index = 0
        x, y = level, level
        Map[x][y] = line[index]
        index += 1
        # 밑으로
        while x + 1 < N - level:
            x += 1
            Map[x][y] = line[index]
            index += 1
        # 오른쪽으로
        while y + 1 < M - level:
            y += 1
            Map[x][y] = line[index]
            index += 1
        # 위로
        while x - 1 >= level:
            x -= 1
            Map[x][y] = line[index]
            index += 1
        # 오른쪽으로
        while y - 1 > level:
            y -= 1
            Map[x][y] = line[index]
            index += 1


def rotate():
    lines = split()
    after_lines = []
    for line in lines:
        move_index = R % len(line)
        after_lines.append(line[-move_index:] + line[:-move_index])
    fill(after_lines)


N, M, R = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
rotate()
for m in Map:
    print(*m)
