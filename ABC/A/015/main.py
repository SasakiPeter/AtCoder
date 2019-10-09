# a, b = [input() for _ in range(2)]
# print([a, b][len(a) < len(b)])

# IQ200 戦略
# maxは何を基準に大きいかを決めるkeyという引数を持っている
# defaultでは、辞書順になってしまう文字列も、これで長さで比べられる
print(max(input(), input(), key=len))
