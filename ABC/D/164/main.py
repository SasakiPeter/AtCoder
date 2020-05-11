s = input()
MOD = 2019
cnt = [0]*MOD
# 番兵、最初に0がないと区間にならない
cnt[0] = 1
cum = 0
for n, x in enumerate(reversed(s)):
    cum = (cum + int(x)*pow(10, n, MOD)) % MOD
    cnt[cum] += 1
print(sum(v*(v-1)//2 for v in cnt))


# # あまりが0の時は、１点でも区間として成立するから、
# # v*(v+1)//2になる　仕切り棒入れて２つとる
# # これは、dd[0]=1で初期化するのと等価
# from collections import defaultdict
# s = input()
# n = len(s)
# p = 2019
# dd = defaultdict(int)
# dd[0] = 1
# prev = 0
# for i in reversed(range(n)):
#     prev = (prev+int(s[i])*pow(10, n-i, p)) % p
#     dd[prev] += 1
# print(sum(v*(v-1)//2 for v in dd.values()))


# #!/usr/bin/env python3
# from collections import defaultdict
# p = 2019
# s = input()
# n = len(s)
# dd = defaultdict(int)
# digits = 0
# prev = 0
# for i in reversed(range(n)):
#     # これをそのままintに変換すると間に合わないので
#     x = (prev+int(s[i])*pow(10, digits, p)) % p
#     dd[x] += 1
#     prev = x
#     digits += 1
# ans = 0
# for k, v in dd.items():
#     if k == 0:
#         ans += v
#     ans += v*(v-1)//2
# print(ans)
