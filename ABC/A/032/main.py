a, b, n = [int(input()) for _ in range(3)]

# whileに条件式直接入れちゃえ！！！！
# while True:
#     if n % a == 0 and n % b == 0:
#         print(n)
#         break
#     n += 1

# while n % a != 0 or n % b != 0:
#     n += 1
# print(n)

while n % a or n % b:
    n += 1
print(n)
