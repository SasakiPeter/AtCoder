s = list(input())
q = int(input())

head = []
tail = []

flip = 0
for _ in range(q):
    com, *query = input().split()
    if com == "1":
        flip ^= 1
    else:
        f, c = query
        f = int(f)-1
        if f ^ flip == 0:
            head.append(c)
        else:
            tail.append(c)

if flip:
    head, tail = tail[::-1], head
    s = s[::-1]
else:
    head = head[::-1]
print("".join(head+s+tail))


# using deque
# from collections import deque

# s = deque(input())
# q = int(input())
# flip = 0
# for _ in range(q):
#     com, *query = input().split()
#     if com == "1":
#         flip ^= 1
#     else:
#         f, c = query
#         f = int(f)-1
#         if f ^ flip == 1:
#             s.append(c)
#         else:
#             s.appendleft(c)
# s = "".join(s)
# print(s if not flip else s[::-1])
