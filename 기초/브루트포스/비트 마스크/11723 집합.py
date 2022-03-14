import sys
s = set()
for _ in range(int(input())):
    oper = sys.stdin.readline().strip().split()
    if len(oper) == 1:
        if oper[0] == "all":
            s = {i for i in range(1,21)}
        elif oper[0] == "empty":
            s = set()
    else:
        oper, val = oper[0], int(oper[1])
        if oper == "add":
            s.add(val)
        elif oper == "remove":
            s.discard(val)
        elif oper == "check":
            print(1 if val in s else 0)
        elif oper == "toggle":
            if val in s:
                s.discard(val)
            else:
                s.add(val)
