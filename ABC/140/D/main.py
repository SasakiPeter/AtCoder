# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# n, k = map(int, input().split())
# s = input().rstrip()


# シミュレーションするなら、この考え方は大いにアリだった
# def split(s):
#     new = [s[0]]
#     for i in range(n-1):
#         if s[i] != s[i+1]:
#             new.append(s[i+1])
#         else:
#             new[-1] += s[i+1]
#     return new


# def transform(s, k):
#     for _ in range(k):
#         s = split(s)
#         if len(s) == 1:
#             s = ''.join(s)
#             break
#         # 要素の大きさはスコアに全く関係なかった
#         # 重要なのは端か、端でないかだけであった
# 　　　　　# この記述だとWAが出る
#         ls = list(map(len, s))
#         idx = ls.index(min(ls))
#         if idx == 0:
#             idx = ls[1:].index(min(ls[1:]))+1

#         # print(s, idx, ls)
#         s[idx] = s[idx].replace('L', 'X').replace('R', 'L').replace('X', 'R')
#         s = ''.join(s)
#     # print(s)
#     return s


# こちらはTLEのみ
# def transform(s, k):
#     for _ in range(k):
#         # ランレングス圧縮っていうらしい
#         # ここで２重ループはきつい
#         # ２重できついとわかっていたなら、なぜもっと考察しなかったのか
#         s = split(s)
#         if len(s) == 1:
#             # 実はこの時ってスコアn-1って決まっている
#             s = ''.join(s)
#             break
#         idx = 1
#         # print(s, idx, ls)
#         s[idx] = s[idx].replace('L', 'X').replace('R', 'L').replace('X', 'R')
#         s = ''.join(s)
#     # print(s)
#     return s


# s = transform(s, k)


# １重ループのここだけだとクソ早い
# 初期スコア導出もっと簡単にできる
# def count(s):
#     cnt = 0
#     for i in range(n):
#         if i+1 < n and s[i] == 'R' and s[i+1] == 'R':
#             cnt += 1
#         elif i-1 >= 0 and s[i] == 'L' and s[i-1] == 'L':
#             cnt += 1
#     return cnt


# 'LRLRRL'
# def count(s):
#     cnt = 0
#     for i in range(n-1):
#         if s[i] == s[i+1]:
#             cnt += 1
#     return cnt

# print(count(s))

n, k = map(int, input().split())
s = input()
print(min(sum(s[i] == s[i+1] for i in range(n-1))+2*k, n-1))
