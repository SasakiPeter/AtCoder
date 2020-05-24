s = input()
n = len(s)
K = int(input())

# import random
# n = 5000
# s = ""
# for _ in range(n):
#     s += chr(96+random.randint(1, 26))

# K = 5
ans = set()

# Kがとても小さいから、そんなに長い部分文字列は必要なさそう
for i in range(n):
    # 長させいぜい10でいいんじゃないか？
    # end = min(n, i+10)
    end = min(n, i+K)
    for j in range(i+1, end+1):
        # print(s[i:j])
        ans.add(s[i:j])

print(sorted(list(ans))[K-1])
