# indexだけ追っていくのが正解
s = input()
L = 0
R = len(s)-1
ans = 0
while L < R:
    if s[L] == s[R]:
        L += 1
        R -= 1
    elif s[L] == 'x' and s[R] != 'x':
        ans += 1
        L += 1
    elif s[L] != 'x' and s[R] == 'x':
        ans += 1
        R -= 1
    elif s[L] != 'x' and s[R] != 'x':
        ans = -1
        break
print(ans)

# # 解答見てシミュレーションしたやつ
# # シミュレーションすると、空になる時の場合わけ考えるのがめんどい
# from collections import deque

# s = deque(input())
# ans = 0
# while s:
#     # 判定してから取り出すのが定石
#     L = s[0]
#     R = s[-1]
#     if L == R:
#         if 1 == len(s):
#             break
#         L = s.popleft()
#         R = s.pop()
#         continue
#     elif L == 'x' and R != 'x':
#         ans += 1
#         s.append('x')
#     elif L != 'x' and R == 'x':
#         ans += 1
#         s.appendleft('x')
#     elif L != 'x' and R != 'x':
#         ans = -1
#         break
# print(ans)

# 自力で実装したやつ
# from collections import deque

# s = input()
# s2 = s.replace('x', '')
# if s2 != s2[::-1]:
#     print(-1)
# else:
#     d = deque(s)
#     a, b = [], []
#     cnt = 0
#     x = y = ''
#     x_skip = y_skip = 0
#     while d:
#         if not x_skip:
#             x = d.popleft()
#         if 0 < len(d) and not y_skip:
#             y = d.pop()

#         if y == '':
#             break

#         if x == y != 'x':
#             cnt += abs(len(a)-len(b))
#             # print("hoge", d, cnt, a, b)
#             x = y = ''
#             a, b = [], []
#             x_skip = y_skip = 0
#             continue

#         if x == 'x':
#             a.append(x)
#         else:
#             x_skip = 1

#         if y == 'x':
#             b.append('x')
#         else:
#             y_skip = 1
#         # print(x, y, d, cnt, a, b)
#     else:
#         # print(d, a, b)
#         cnt += abs(len(a)-len(b))

#     print(cnt)


#     center = s2[len(s2)//2]
#     # 真ん中の文字が、元の文字列の中でどの辺にあるか
#     # ここ、がっつり条件分けないとむり
#     cnt = s.count(center)//2 + 1
#     for i, c in enumerate(s):
#         if c == center:
#             cnt -= 1
#         if cnt == 0:
#             center_idx = i
#             break
#     if not (len(s2) & 1):
#         front = list(s)[:center_idx]
#         rear = list(s)[center_idx+1:][::-1]
#     else:
#         front = list(s)[:center_idx-1]
#         rear = list(s)[center_idx+1:][::-1]

#     if len(front) == 0 or len(rear) == 0:
#         print(max(len(front), len(rear)))
#     else:
#         a, b = front.pop(), rear.pop()
#         cnt = 0
#         print(a, b, front, rear)
#         # while True:
#         #     # print(a, b, front, rear)
#         #     if a == b == 'x':
#         #         if 0 < len(front) <= len(rear):
#         #             a = front.pop()
#         #             b = rear.pop()
#         #         else:
#         #             if 0 == len(front) == len(rear):
#         #                 break
#         #             if 0 < len(front):
#         #                 a = front.pop()
#         #                 cnt += 1
#         #             if 0 < len(rear):
#         #                 b = rear.pop()
#         #                 cnt += 1
#         #             # continue

#         #     if a == b:
#         #         if 0 < len(front):
#         #             a = front.pop()
#         #         if 0 < len(rear):
#         #             b = rear.pop()

#         #         # continue
#         #     if a == 'x' and b != 'x':
#         #         cnt += 1
#         #         if 0 < len(front):
#         #             a = front.pop()
#         #     if a != 'x' and b == 'x':
#         #         cnt += 1
#         #         if 0 < len(rear):
#         #             b = rear.pop()
#         #     if len(front) == 0 and len(rear) == 0:
#         # break
#         # print("hgoe")
#         print(cnt)

# # built-in objectにはメソッドを追加できない
# # str.is_kaibun = lambda self: self.__str__() == self.__str__()[::-1]
# # print(kaibun.is_kaibun())


# # def is_kaibun(s):
# #     return s == s[::-1]
