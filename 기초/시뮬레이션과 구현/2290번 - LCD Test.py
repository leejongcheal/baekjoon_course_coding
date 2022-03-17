"""
 1
2 3
 4    그려주는 함수들
5 6
 7
"""


def fill_1(number, N, M, s):
    for j in range(1, M - 1):
        number[0][j] = '-'


def fill_2(number, N, M, s):
    for i in range(1, s + 1):
        number[i][0] = "|"


def fill_3(number, N, M, s):
    for i in range(1, s + 1):
        number[i][M - 1] = "|"


def fill_4(number, N, M, s):
    for j in range(1, M - 1):
        number[s + 1][j] = "-"


def fill_5(number, N, M, s):
    for i in range(s + 2, N - 1):
        number[i][0] = "|"


def fill_6(number, N, M, s):
    for i in range(s + 2, N - 1):
        number[i][M - 1] = "|"


def fill_7(number, N, M, s):
    for j in range(1, M - 1):
        number[N - 1][j] = "-"


def make_number(numbers, N, M, s):
    # 0 만들기
    number = numbers[0]
    fill_1(number, N, M, s)
    fill_2(number, N, M, s)
    fill_3(number, N, M, s)
    fill_5(number, N, M, s)
    fill_6(number, N, M, s)
    fill_7(number, N, M, s)
    # 1만들기
    number = numbers[1]
    fill_3(number, N, M, s)
    fill_6(number, N, M, s)
    # 2만들기
    number = numbers[2]
    fill_1(number, N, M, s)
    fill_3(number, N, M, s)
    fill_4(number, N, M, s)
    fill_5(number, N, M, s)
    fill_7(number, N, M, s)
    # 3만들기
    number = numbers[3]
    fill_1(number, N, M, s)
    fill_3(number, N, M, s)
    fill_4(number, N, M, s)
    fill_6(number, N, M, s)
    fill_7(number, N, M, s)
    # 4만들기
    number = numbers[4]
    fill_2(number, N, M, s)
    fill_3(number, N, M, s)
    fill_4(number, N, M, s)
    fill_6(number, N, M, s)
    # 5만들기
    number = numbers[5]
    fill_1(number, N, M, s)
    fill_2(number, N, M, s)
    fill_4(number, N, M, s)
    fill_6(number, N, M, s)
    fill_7(number, N, M, s)
    # 6만들기
    number = numbers[6]
    fill_1(number, N, M, s)
    fill_2(number, N, M, s)
    fill_4(number, N, M, s)
    fill_5(number, N, M, s)
    fill_6(number, N, M, s)
    fill_7(number, N, M, s)
    # 7만들기
    number = numbers[7]
    fill_1(number, N, M, s)
    fill_3(number, N, M, s)
    fill_6(number, N, M, s)
    # 8만들기
    number = numbers[8]
    fill_1(number, N, M, s)
    fill_2(number, N, M, s)
    fill_3(number, N, M, s)
    fill_4(number, N, M, s)
    fill_5(number, N, M, s)
    fill_6(number, N, M, s)
    fill_7(number, N, M, s)
    # 9만들기
    number = numbers[9]
    fill_1(number, N, M, s)
    fill_2(number, N, M, s)
    fill_3(number, N, M, s)
    fill_4(number, N, M, s)
    fill_6(number, N, M, s)
    fill_7(number, N, M, s)


s, L = input().split()
s = int(s)
L = list(map(int, list(L)))

N = 2 * s + 3
M = s + 2
numbers = []
res = [[] for _ in range(N)]
blank = [[" "] for _ in range(N)]
for i in range(10):
    numbers.append([[" "] * M for _ in range(N)])
make_number(numbers, N, M, s)
for l in L:
    number = numbers[l]
    for i in range(N):
        res[i] += number[i] + blank[i]
for r in res:
    print("".join(r))