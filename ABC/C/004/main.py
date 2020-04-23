n = int(input())
cards = [1, 2, 3, 4, 5, 6]

# 10**9だから、for回すだけで、死ぬ
n %= 30
for i in range(n):
    i %= 5
    cards[i], cards[i+1] = cards[i+1], cards[i]


print("".join(map(str, cards)))
