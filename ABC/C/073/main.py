n = int(input())
a = set()
for _ in range(n):
    a ^= {int(input())}
print(len(a))

# これ、めっちゃ使えそう


# 他の解法としては、全部リストかなんかに格納した後に、
# 奇数回出現するものの数だけ出力するというのが考えられる
# 実装してみる
# from collections import defaultdict

# n = int(input())
# a = defaultdict(int)
# for _ in range(n):
#     a[int(input())] += 1
# # maxはO(n)
# # print(sum(v % 2 for v in a.values()))
# # lenはO(1)
# print(len([1 for v in a.values() if v % 2]))
