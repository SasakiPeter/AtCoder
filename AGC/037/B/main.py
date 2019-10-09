import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
s = input().rstrip()
mod = 998244353

dic = {'R': 0, 'G': 0, 'B': 0}

answer = 1
for x in s:
    f, s, t = sorted(dic.values())
    if dic[x] < s:
        answer *= s - dic[x]
    elif dic[x] < t:
        answer *= t - s
    # t<=dic[x]
    else:
        answer *= n - dic[x]
    dic[x] += 1
    answer %= mod

print(answer % mod)


# for x in s:
#     f, s, t = sorted(dic.values())
#     # 足す時に他の色より個数が劣っていたら、
#     # 劣っている数だけしか自由度はない
#     # 劣っている時は、他の二色を見て、もっとも劣っているほうが
#     # 計算すべき自由度
#     # ただし、0の時は
#     if dic[x] < s:
#         answer *= s-dic[x]
#         # print(answer, x, s-dic[x], '1')
#     elif dic[x] < t:
#         answer *= t-s
#         # print(answer, x, t-s, '2')
#     dic[x] += 1
#     # 足した結果、他のどの色よりも大きくなってしまった場合は、
#     # n-c[x]+1の自由度
#     if t < dic[x]:
#         answer *= n - dic[x] + 1
#         # print(answer, x, n - dic[x] + 1, '3')
