n, k = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))

history = [-1]*n
ans = []
cur = 0
for i in range(n):
    if history[cur] != -1:
        init_cnt = history[cur]
        loop_cnt = i - history[cur]
        break
    history[cur] = i
    ans.append(cur+1)
    cur = A[cur]

# print(history, init_cnt, loop_cnt)

loop = k if k <= init_cnt else init_cnt+((k-init_cnt) % loop_cnt)
print(ans[loop])
# なぜかこっちの方が早いっていう↓
# print(history.index(loop)+1)


# # ダブリング　高速（pypy）
# n, k = map(int, input().split())
# A = list(map(lambda x: int(x)-1, input().split()))
# bit = k.bit_length()
# table = [[0]*n for _ in range(bit)]
# table[0] = A

# for i in range(1, bit):
#     for j in range(n):
#         table[i][j] = table[i-1][table[i-1][j]]

# ans = 0
# for i in reversed(range(bit)):
#     if (1 << i) <= k:
#         k -= 1 << i
#         ans = table[i][ans]
# print(ans+1)


# # ダブリング めちゃくちゃ遅い
# n, k = map(int, input().split())
# A = list(map(lambda x: int(x)-1, input().split()))
# bit = k.bit_length()
# table = [[0]*bit for _ in range(n)]
# for i in range(n):
#     table[i][0] = A[i]

# for i in range(1, bit):
#     for j in range(n):
#         table[j][i] = table[table[j][i-1]][i-1]

# ans = 0
# for i in reversed(range(bit)):
#     if (1 << i) <= k:
#         k -= 1 << i
#         ans = table[ans][i]
# print(ans+1)


# 最初に思いついた方法
# import sys
# from collections import Counter
# sys.setrecursionlimit(10**7)
# n, k = map(int, input().split())
# A = list(map(lambda x: int(x)-1, input().split()))

# visited = [0]*n


# def teleport(v):
#     if visited[v]+1 == 3:
#         return 0
#     visited[v] += 1
#     teleport(A[v])


# teleport(0)
# c = Counter(visited)
# init = c[1]
# loop_cnt = c[2]

# if k <= init:
#     min_k = k
# else:
#     min_k = init + ((k-init) % loop_cnt)

# ans = 0
# for _ in range(min_k):
#     ans = A[ans]
# print(ans+1)
