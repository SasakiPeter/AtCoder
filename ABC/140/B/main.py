n = int(input())
a, b, c = [list(map(int, input().split())) for _ in range(3)]

ans = sum(b)

# 焦った時によく使う前の値を記憶しておく処理は、
# indexでfor文を回すか、zipで2つ同時に値を取り出すかすれば
# 問題解決であった
# last = -1
# for x in a:
#     if last+1 == x:
#         ans += c[last-1]
#     last = x
# print(ans)


# for i, x in enumerate(a):
#     if i+1 < len(a) and a[i] == a[i+1]-1:
#         ans += c[a[i]-1]
# print(ans)

# for i in range(len(a)-1):
#     if a[i] == a[i+1]-1:
#         ans += c[a[i]-1]
# print(ans)


# zipは少ない方のリスト分しか取り出せないので、
# a[:-1]はaでもいいっていう
for x, y in zip(a[:-1], a[1:]):
    if x + 1 == y:
        ans += c[x-1]
print(ans)
