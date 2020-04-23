from collections import defaultdict

n, p = map(int, input().split())
s = input()

if p in (2, 5):
    if p == 2:
        ok_list = [i for i in range(10)][::2]
    else:
        ok_list = [0, 5]
    ans = 0
    for i in range(n):
        if int(s[i]) in ok_list:
            ans += i+1
    print(ans)
else:
    dd = defaultdict(int)
    dd[0] = 1
    prev = 0

    for i in range(n-1, -1, -1):
        # デカイ数のintと%が重い
        # dd[int(s[i:]) % p] += 1

        # 543 mod(3) ≡ 500 + 43 (mod 3) ≡ 500 (mod 3) + 43 (mod3)
        # ↓TLE
        # d = int(s[i]) * (10**(n-i) % p)
        # ↓AC
        d = int(s[i]) * pow(10, n-i, p)
        prev = (prev + d) % p
        dd[prev] += 1

    # 543 ≡ 3 (mod 3) → (543 - 3)%3 = 0
    print(sum(v*(v-1)//2 for v in dd.values()))


# ans = 0
# # 絶対に間に合わない全探索
# for i in range(n):
#     for j in range(i+1, n+1):
#         if int(s[i:j]) % p == 0:
#             ans += 1

# print(ans)
