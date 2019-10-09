# from collections import Counter

# n = int(input())
# a = list(map(int, input().split()))
# # 0の個数を計算しないといけない
# d = Counter(a)
# print(-(-sum(a)//(n-d[0])))

n = int(input())
a = list(map(int, input().split()))
print(-(-sum(a)//(n-a.count(0))))

# list.count(0) っていう便利なものあるやん！！

# -~(5+5)//2 みたいな繰り上げ処理は、2で割る時しかうまくいかない
