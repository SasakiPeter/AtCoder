from collections import Counter
b = [input() for _ in range(int(input()))]
r = [input() for _ in range(int(input()))]

db, dr = [Counter(x) for x in (b, r)]
print(max(*[v-dr[k] for k, v in db.items()]+[0]))


# b = [input() for _ in range(int(input()))]
# r = [input() for _ in range(int(input()))]
# l = list(set(b))
# # listのcountを使って、要素数を取得できる　これ便利
# print(max(0, max(b.count(x)-r.count(x) for x in l)))

# 0910
n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
print(max(0, max(s.count(w)-t.count(w) for w in set(s))))
