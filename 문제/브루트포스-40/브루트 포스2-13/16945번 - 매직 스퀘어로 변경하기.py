def cal(square, Map):
    val = 0
    for i in range(3):
        for j in range(3):
            val += abs(Map[i][j] - square[i][j])
    return val

time_square = [[[2, 7, 6], [9, 5, 1], [4, 3, 8]], [[2, 9, 4], [7, 5, 3], [6, 1, 8]], [[4, 3, 8], [9, 5, 1], [2, 7, 6]], [[4, 9, 2], [3, 5, 7], [8, 1, 6]], [[6, 1, 8], [7, 5, 3], [2, 9, 4]], [[6, 7, 2], [1, 5, 9], [8, 3, 4]], [[8, 1, 6], [3, 5, 7], [4, 9, 2]], [[8, 3, 4], [1, 5, 9], [6, 7, 2]]]
Map = [list(map(int, input().split())) for _ in range(3)]
visit = []
res = int(1e10)
for square in time_square:
    res = min(res, cal(square, Map))
print(res)