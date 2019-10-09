a, b = map(int, input().split())
a = (a+11) % 13
b = (b+11) % 13
print('Alice' if a > b else 'Bob' if a < b else 'Draw')

# if a == b:
#     print('Draw')
# elif a == 1 or b == 1:
#     print('Alice' if a < b else 'Bob')
# else:
#     print('Alice' if a > b else 'Bob')


# この記述で、2~13を0~11にずらすことができる 1は12になる
# print('Draw' if a == b else 'Alice' if (a+11) % 13 > (b+11) % 13 else 'Bob')
