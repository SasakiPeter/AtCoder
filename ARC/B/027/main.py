import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


class UnionFind:
    def __init__(self, n):
        self.p = [-1]*n
        self.r = [1]*n

    def find(self, x):
        if self.p[x] < 0:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.r[rx] > self.r[ry]:
                rx, ry = ry, rx
            if self.r[rx] == self.r[ry]:
                self.r[ry] += 1
            self.p[ry] += self.p[rx]
            self.p[rx] = ry


n = int(input())
s1 = input()
s2 = input()


def to_idx(x):
    return ord(x)-ord('A')


uf = UnionFind(26)
for x, y in zip(s1, s2):
    if not x.isalpha() or not y.isalpha():
        continue
    uf.union(to_idx(x), to_idx(y))

used_parent = [0]*26
for i, (x, y) in enumerate(zip(s1, s2)):
    x, y = map(to_idx, (x, y))

    if not 0 <= x < 26 and not 0 <= y < 26:
        continue
    elif not 0 <= x < 26 and 0 <= y < 26:
        y_parent = uf.find(y)
        used_parent[y_parent] = 1
    elif not 0 <= y < 26 and 0 <= x < 26:
        x_parent = uf.find(x)
        used_parent[x_parent] = 1
    else:
        x_parent = uf.find(x)
        y_parent = uf.find(y)
        val = 9 if i == 0 else 10
        if not used_parent[x_parent]:
            used_parent[x_parent] = val
        if not used_parent[y_parent]:
            used_parent[y_parent] = val

# print(used_parent)

ans = 1
for x in used_parent:
    if x:
        ans *= x
print(ans)


# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)


# class UnionFind:
#     def __init__(self, n):
#         self.p = [-1]*n
#         self.r = [1]*n

#     def find(self, x):
#         if self.p[x] < 0:
#             return x
#         else:
#             self.p[x] = self.find(self.p[x])
#             return self.p[x]

#     def union(self, x, y):
#         rx, ry = self.find(x), self.find(y)
#         if rx != ry:
#             if self.r[rx] > self.r[ry]:
#                 rx, ry = ry, rx
#             if self.r[rx] == self.r[ry]:
#                 self.r[ry] += 1
#             self.p[ry] += self.p[rx]
#             self.p[rx] = ry

#     def same(self, x, y):
#         return self.find(x) == self.find(y)

#     def count_members(self, x):
#         return -self.p[self.find(x)]

#     def count_roots(self):
#         return sum(p < 0 for p in self.p)


# n = int(input())
# s1 = input()
# s2 = input()

# alpha = set(map(chr, range(ord('A'), ord('Z')+1)))
# uf = UnionFind(26)
# for x, y in zip(s1, s2):
#     # xとyが親に数字を紐付けたい
#     if x not in alpha or y not in alpha:
#         continue
#     uf.union(ord(x)-ord('A'), ord(y)-ord('A'))
# used_parent = [0]*26
# for i, (x, y) in enumerate(zip(s1, s2)):
#     if x not in alpha and y in alpha:
#         y_parent = uf.find(ord(y)-ord('A'))
#         used_parent[y_parent] = x
#     elif y not in alpha and x in alpha:
#         x_parent = uf.find(ord(x)-ord('A'))
#         used_parent[x_parent] = y
#     elif x not in alpha and y not in alpha:
#         continue
#     else:
#         x_parent = uf.find(ord(x)-ord('A'))
#         y_parent = uf.find(ord(y)-ord('A'))
#         if i == 0:
#             x = 'X'
#         else:
#             x = 'Y'
#         if not used_parent[x_parent]:
#             used_parent[x_parent] = x
#         if not used_parent[y_parent]:
#             used_parent[y_parent] = x

# # print(used_parent)

# ans = 1
# for x in used_parent:
#     if x:
#         if x == 'X':
#             ans *= 9
#         elif x == 'Y':
#             ans *= 10
# print(ans)

# from collections import defaultdict
# n = int(input())
# s1 = input()
# s2 = input()

# table = defaultdict(lambda: '')
# alpha = set(map(chr, range(ord('A'), ord('Z')+1)))
# for a in alpha:
#     table[a] = ''

# for x, y in zip(s1, s2):
#     if x not in alpha and y in alpha:
#         table[y] = x
#         for i in range(26):
#             a = chr(ord('A')+i)
#             if table[a] == y:
#                 table[a] = x
#     elif y not in alpha and x in alpha:
#         table[x] = y
#         for i in range(26):
#             a = chr(ord('A')+i)
#             if table[a] == x:
#                 table[a] = y
#     elif x in alpha and y in alpha:
#         if not table[y]:
#             table[y] = x
#             for i in range(26):
#                 a = chr(ord('A')+i)
#                 if table[a] == y:
#                     table[a] = x
#         else:
#             table[x] = table[y]
#             # table[x]になるようなkeyも全て変えないといけない
#             for i in range(26):
#                 a = chr(ord('A')+i)
#                 if table[a] == x:
#                     table[a] = table[y]

# # print(table)

# letter = ['']*n
# # letter2 = ['']*n

# for i, (x, y) in enumerate(zip(s1, s2)):
#     # print(i, x, y, table[x], table[y])
#     if x not in alpha and y not in alpha:
#         letter[i] = x
#         # letter2[i] = x
#     elif table[x]:
#         letter[i] = table[x]
#         # letter2[i] = table[x]
#     elif table[y]:
#         letter[i] = table[y]
#         # table[x] = table[y]
#         # letter2[i] = table[y]
#     else:
#         # 未定のindexは記録しておくべき
#         # そして、そのindexには新しく文字を振り直す
#         # ルールは、同じ文字は同じにする
#         letter[i] = x
#         # letter2[i] = y


# # print(''.join(letter))
# # print(''.join(letter2))
# ans = 1
# used_alpha = [0]*26
# for i in range(n):
#     x = letter[i]
#     if x in alpha:
#         # すでに使用してあったら、何もしない
#         if used_alpha[ord(x)-ord('A')]:
#             continue
#         used_alpha[ord(x)-ord('A')] = 1
#         if i == 0:
#             ans *= 9
#         else:
#             ans *= 10
# print(ans)
# # print(used_alpha)
