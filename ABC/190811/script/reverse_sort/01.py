# ABC047 A - キャンディーと2人の子供 / Fighting over Candies

# 10 30 20
l = [int(x) for x in input().split()]
# なぜかダメ
# print('Yes' if max(l) == sum(l)//2 else 'No')

a, b, c = sorted(l)[::-1]
print('Yes' if b+c == a else 'No')
