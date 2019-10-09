# s = input()
# print(s[0]+str(len(s)-2)+s[-1])

# 文字列の受け取り方を工夫する
a, *b, c = input()
print(a+str(len(b))+c)
