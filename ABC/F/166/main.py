# DFSで書けない？
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, *abc = map(int, input().split())
s = [input().rstrip()for _ in range(n)]
cond = {'AB': (0, 1), 'AC': (0, 2), 'BC': (1, 2)}
legend = ('A', 'B', 'C')
ans = []


def dfs(i):
    if -1 in abc:
        return 0
    elif i == n:
        print('Yes')
        print(*ans, sep='\n')
        exit()
    else:
        idx1, idx2 = cond[s[i]]
        abc[idx1] += 1
        abc[idx2] -= 1
        ans.append(legend[idx1])
        dfs(i+1)
        ans.pop()
        abc[idx1] -= 1
        abc[idx2] += 1

        abc[idx1] -= 1
        abc[idx2] += 1
        ans.append(legend[idx2])
        dfs(i+1)
        ans.pop()
        abc[idx1] += 1
        abc[idx2] -= 1


dfs(0)
print('No')

# n, *abc = map(int, input().split())
# cond = {'AB': (0, 1), 'AC': (0, 2), 'BC': (1, 2)}
# legend = ['A', 'B', 'C']
# ans = []
# prev_s = ''
# for _ in range(n):
#     s = input()
#     idx1, idx2 = cond[s]
#     # ABだったら、ABの小さい方を選択して、
#     # 小さい方に1足して、大きい方から1ひく
#     # さらに、ansに小さい方を追加する
#     if abc[idx1] == abc[idx2] == 0 and ans:
#         prev_x = ans.pop()
#         if prev_x == prev_s[0]:
#             prev_y = prev_s[1]
#         else:
#             prev_y = prev_s[0]
#         ans.append(prev_y)
#         abc[legend.index(prev_x)] -= 2
#         abc[legend.index(prev_y)] += 2

#     if abc[idx1] < abc[idx2]:
#         abc[idx1] += 1
#         abc[idx2] -= 1
#         ans.append(legend[idx1])
#     else:
#         abc[idx2] += 1
#         abc[idx1] -= 1
#         ans.append(legend[idx2])
#     prev_s = s
#     if -1 in abc:
#         print('No')
#         break
# else:
#     print('Yes')
#     for x in ans:
#         print(x)


# # 0を回避するように構築
# n, a, b, c = map(int, input().split())
# ans = []
# prev = ''
# for _ in range(n):
#     s = input()
#     if 'C' not in s:
#         # a,b両方0みたいなときに困る
#         # そういう場合、そうならないように選択を変えておく必要がある
#         # キングクリムゾンの能力が必要
#         if a == b == 0 and ans:
#             # キングクリムゾン発動！
#             prev_x = ans.pop()
#             if prev_x == prev[0]:
#                 prev_y = prev[1]
#             else:
#                 prev_y = prev[0]
#             ans.append(prev_y)
#             if prev_x == 'A':
#                 a -= 2
#             elif prev_x == 'B':
#                 b -= 2
#             else:
#                 c -= 2
#             if prev_y == 'A':
#                 a += 2
#             elif prev_y == 'B':
#                 b += 2
#             else:
#                 c += 2
#         if a < b:
#             a += 1
#             b -= 1
#             ans.append('A')
#         else:
#             a -= 1
#             b += 1
#             ans.append('B')

#     elif 'B' not in s:
#         if a == c == 0 and ans:
#             # キングクリムゾン発動！
#             prev_x = ans.pop()
#             if prev_x == prev[0]:
#                 prev_y = prev[1]
#             else:
#                 prev_y = prev[0]
#             ans.append(prev_y)

#             if prev_x == 'A':
#                 a -= 2
#             elif prev_x == 'B':
#                 b -= 2
#             else:
#                 c -= 2
#             if prev_y == 'A':
#                 a += 2
#             elif prev_y == 'B':
#                 b += 2
#             else:
#                 c += 2
#         if a < c:
#             a += 1
#             c -= 1
#             ans.append('A')
#         else:
#             a -= 1
#             c += 1
#             ans.append('C')
#     elif 'A' not in s:
#         if b == c == 0 and ans:
#             # キングクリムゾン発動！
#             prev_x = ans.pop()
#             if prev_x == prev[0]:
#                 prev_y = prev[1]
#             else:
#                 prev_y = prev[0]
#             ans.append(prev_y)
#             if prev_x == 'A':
#                 a -= 2
#             elif prev_x == 'B':
#                 b -= 2
#             else:
#                 c -= 2
#             if prev_y == 'A':
#                 a += 2
#             elif prev_y == 'B':
#                 b += 2
#             else:
#                 c += 2
#         if b < c:
#             b += 1
#             c -= 1
#             ans.append('B')
#         else:
#             b -= 1
#             c += 1
#             ans.append('C')
#     prev = s
#     # 負の数になってしまったときに、時間を巻き戻したい
#     # これは経過を見ていないので、途中で負になっているかもしれない
#     if -1 in (a, b, c):
#         print('No')
#         break
# else:
#     print('Yes')
#     for x in ans:
#         print(x)
