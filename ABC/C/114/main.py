N = int(input())
# for縛り
# if n < 3:
#     print(0)
# elif n > 3:
#     #
#     print(6*2)


# 全部を洗い出すのは無理なので、準753数を数え上げる
# どのように列挙するか、考えてみる


# 再帰関数を使って数え上げ
def dfs(x):
    if int('0'+x) > N:
        return 0

    retval = 1 if len(set(x)) == 3 else 0
    for c in '753':
        retval += dfs(x + c)
    return retval


print(dfs(''))

# 4進数を使って、数え上げ

# def squ(x):
#     if x == 0:
#         return '0'
#     a = ""
#     while x != 0:
#         x, mod = divmod(x, 4)
#         a += str(mod)
#     return a[::-1]

# # def tri(x):
# #     if x == 0:
# #         return '0'
# #     a = ""
# #     # mod = -1
# #     while x != 0:
# #         x, mod = divmod(x, 3)
# #         a += str(mod)
# #     return a[::-1]


# ans = 0

# for x in range(10**6):
#     # 3進数に変換
#     # x_tri = tri(x)
#     # x_str = x_tri.replace('0', '3').replace('1', '5').replace('2', '7')
#     x_squ = squ(x)
#     x_str = x_squ.replace('3', '7').replace('2', '5').replace('1', '3')

#     if "0" in x_str:
#         continue

#     if int(x_str) > n:
#         break

#     if len(set(x_str)) != 3:
#         continue

#     ans += 1

# print(ans)

# ans = 0
# for i in range(1, n+1):
#     s = set(str(i))
#     if all(x in '753' for x in s) and len(s) == 3:
#         ans += 1
# print(ans)
