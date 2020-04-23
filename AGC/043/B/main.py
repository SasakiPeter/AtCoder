n = int(input())
A = list(map(int, list(input())))
# n = 10**5
# A = list(map(int, list("12312"*(n//5))))
ans = 0
prev = [A[0]]
for a in A[1:]:
    loop = len(prev)
    for i in range(loop):
        x = prev[i]
        prev[i] = a
        a = abs(x-a)
        if i == loop-1:
            prev.append(a)
print(prev[-1])

# ans = 0
# prev = [A[0]]
# loop = [0, 1]
# cnt = 1
# for a in A[1:]:
#     # tmp = [a]
#     print(prev, loop)
#     prev.append(a)
#     for idx in range(*loop):
#         print(idx)
#         a = abs(a-prev[idx])
#         # tmp.append(a)
#         prev.append(a)
#     cnt += 1
#     loop[0] = loop[1]
#     loop[1] = loop[0]+cnt
#     # prev = tmp
# print(prev[-1])
