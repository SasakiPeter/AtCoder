s = input()
print(s.count('BW') + s.count("WB"))

# s = input()
# prev = ans = -1
# for c in s:
#     if prev != c:
#         prev = c
#         ans += 1
# print(ans)

# # グループに分けることができれば勝ち
# # 無駄に、リストとか使うと重い
# prev = ""
# ls = []
# for c in s:
#     if c != prev:
#         prev = c
#         ls.append(c)
#     else:
#         ls[-1] += c

# print(len(ls)-1)
