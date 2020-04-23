# from collections import Counter
s = input()
t = input()


# 矛盾を導けばいい
TABLE = {a: "" for a in map(chr, range(97, 123))}

for x, y in zip(s, t):
    if TABLE[x] == "":
        if y not in TABLE.values():
            TABLE[x] = y

    if TABLE[x] != y:
        print("No")
        break
else:
    print("Yes")


# print(TABLE)

# 矛盾がないか調べる


# if len(set(s)) == len(set(t)):
#     print("Yes")
#     # 2種類以上存在するものは、場所があってないといけない
#     sc = Counter(s)
#     tc = Counter(t)
#     sls = [(k, v)for k, v in sorted(
#         sc.items(), key=lambda x: x[1], reverse=True) if v > 1]
#     tls = [(k, v)for k, v in sorted(
#         tc.items(), key=lambda x: x[1], reverse=True) if v > 1]
#     print(sls, tls)

# else:
#     print("No")
