# さらに考察した結果　一発AC　気持ちいい
n, k = map(int, input().split())
n_mod0 = n//k

if k % 2:
    print(n_mod0**3)
else:
    n_modk2 = (n+(k//2))//k
    print(n_mod0**3 + n_modk2**3)

# 初期実装
# from collections import defaultdict
# n, k = map(int, input().split())
# dd = defaultdict(list)
# for i in range(1, n+1):
#     dd[i % k].append(i)


# if k % 2:
#     print(len(dd[0])**3)
# else:
#     print(len(dd[0])**3 + len(dd[k//2])**3)
