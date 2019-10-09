# 理想とするゴールを先に２パターン作って、それと同じになるには
# 何手必要か判定

# s = list(map(int, list(input())))
# e = [i % 2 for i in range(len(s))]
# o = [(i+1) % 2 for i in range(len(s))]
# print(min(sum(x != y for x, y in zip(s, e)), sum(x != y for x, y in zip(s, o))))


s = input()
e = s[::2]
o = s[1::2]
# 偶数番目の0の数と奇数番目の1の数の和は、101みたいのにするときの１つの回だし
# その逆の010にするときは、len(s)-nになる
n = e.count("0") + o.count("1")
print(min(n, len(s)-n))

# 偶数番目を取得
# print(s[::2])

# 奇数番目を取得
# print(s[1::2])
