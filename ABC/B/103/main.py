s, t = [input() for _ in range(2)]
print('Yes' if any(t == s[len(s)-1-i:]+s[0:len(s)-1-i]
                   for i in range(len(s))) else 'No')

# 唖然とした回答
# 2回繰り返せば、あるかどうかわかるよねっていう
# print('Yes' if input() in input()*2 else 'No')
