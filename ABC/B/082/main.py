s = ''.join(sorted(input()))
t = ''.join(sorted(input())[::-1])
# # なりうればYesなので、ソートしても意味ない
# # sの方は意味あると思うけど

# # 全探索の方がいい？
print('Yes' if s < t else 'No')


# 全探索
# sだけソートして、tは並び替える
# tの並び替えられる場合の数はlen(t)! tは逆順にソートすればいい
# s, t = []


# リストの比較もできるらしい
# print('Yes' if sorted(input()) < sorted(input())[::-1] else 'No')
