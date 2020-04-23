s = input()
s = s.replace("eraser", "").replace("erase", "").replace(
    "dreamer", "").replace("dream", "")

# print(s)
# if s == "":
#     print("YES")
# else:
#     print("NO")

print("NO" if s else "YES")

# これは草
# print("YNEOS"[s > ''::2])
