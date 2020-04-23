from collections import deque

s = deque(input())
q = int(input())

inv = False
for _ in range(q):
    com, *query = input().split()
    if com == "1":
        if not inv:
            inv = True
        else:
            inv = False
    else:
        f, c = query
        if not inv:
            if f == "1":
                s.appendleft(c)
            else:
                s.append(c)
        else:
            if f == "1":
                s.append(c)
            else:
                s.appendleft(c)


s = "".join(s)
print(s if not inv else s[::-1])
