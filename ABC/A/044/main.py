n, k, x, y = [int(input()) for _ in range(4)]
# print(k*x+(n-k)*y if n >= k else n*x)

# if を使わないようにするには、max()で条件分ければいい
# 差分だけ足すような処理にする
print(n*x + (y-x)*max(n-k, 0))
