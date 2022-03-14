s = set()
for _ in range(int(input())):
    oper = input().split()
    if len(oper) > 1:
        oper, val = oper[0], int(oper[1])
        if oper == "add":
            s.add(val)
        elif oper == "remove":
            if val in s:
                s.remove(val)
        elif oper == "check":
            if val in s:
                print(1)
            else:
                print(0)
        elif oper == "toggle":
            if val in s:
                s.remove(val)
            else:
                s.add(val)
    # all, empty
    else:
        if oper[0] == "all":
            s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        elif oper == "empty":
            s = set()