# 逆順にシミュレートすれば良かったらしい
n = int(input())
B = list(map(int, input().split()))
ans = []
for _ in range(n):
    for i in reversed(range(len(B))):
        if B[i] == i+1:
            x = B.pop(i)
            ans.append(x)
            break
if len(ans) == n:
    print(*ans[::-1], sep='\n')
else:
    print(-1)

# n = int(input())
# B = list(map(int, input().split()))
# A = []
# for b in B:
#     A.insert(b-1, b)
# if all(A[i] <= i+1 for i in range(n)):
#     C = []
#     for a in A:
#         C.insert(a-1, a)
#     if B == C:
#         print(*A, sep='\n')
#     else:
#         print(-1)
# else:
#     print(-1)

# # simulationはムリ
# from collections import Counter
# import sys
# sys.setrecursionlimit(10**7)
# n = int(input())
# B = list(map(int, input().split()))
# c = Counter(B)
# A = []
# history = []


# def dfs(i):
#     if i == n+1:
#         if A == B:
#             print(*history, sep='\n')
#             exit()
#         return 0
#     for j in reversed(range(1, i+1)):
#         if not c[j]:
#             continue
#         c[j] -= 1
#         history.append(j)
#         A.insert(j-1, j)
#         dfs(i+1)
#         A.pop(j-1)
#         history.pop()
#         c[j] += 1


# dfs(1)
# print(-1)
