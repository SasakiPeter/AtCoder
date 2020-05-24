from itertools import product
s = input()
n = len(s)
# 3文字以下の部分文字列を列挙する
ts = set()
for i in range(n):
    end = min(n+1, i+4)
    for j in range(i+1, end):
        ts.add(s[i:j])
# print(ts)

ans = set()

for t in ts:
    m = len(t)
    for bit in product((0, 1), repeat=m):
        t_tmp = ""
        for j in range(m):
            if bit[j]:
                t_tmp += '.'
            else:
                t_tmp += t[j]
        ans.add(t_tmp)
print(len(ans))

# import itertools
# # tを全探索する
# s = input()
# n = len(s)
# ts = []
# *strings, = map(chr, range(97, 123))
# strings.append('.')
# strings.append('')

# for perm in itertools.product(strings, repeat=3):
#     t = "".join(perm)
#     if t:
#         ts.append(t)

# ans = 0
# for t in ts:
#     m = len(t)
#     for i in range(n-m):
#         s_tmp = s[i:i+m]
#         print(s_tmp, t, 'hoge')
#         if all(t[j] == '.'or t[j] == s_tmp[j] for j in range(m)):
#             ans += 1
#             print(t, s_tmp, s)
#             break

# print(ans)
