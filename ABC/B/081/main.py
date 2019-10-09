n = int(input())
a = list(map(int, input().split()))

# スマート
cnt = 0
while all(x % 2 == 0 for x in a):
    a = [x//2 for x in a]
    cnt += 1


# while True:
#     if n == sum(1 if x % 2 == 0 else 0 for x in a):
#         a = list(map(lambda x: x//2, a))
#         cnt += 1
#     else:
#         break
print(cnt)


# 9.16
# n = int(input())
# # 10**9
# a = list(map(int, input().split()))
# cnt = 0
# # なんでこれ、実行時間間に合うのかよくわかってない
# while all(x % 2 == 0 for x in a):
#     a = list(map(lambda x: x//2, a))
#     cnt += 1
# print(cnt)
