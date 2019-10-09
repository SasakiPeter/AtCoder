# s = input()
# s = s[0:-2]
# for _ in range(len(s)):
#     h = len(s)//2
#     if s[0:h] == s[h:]:
#         print(len(s))
#         break
#     else:
#         s = s[0:-2]

# whileに条件式突っ込むのとどっちがいいかな？
s = input()[:-2]
while s[:len(s)//2] != s[len(s)//2:]:
    s = s[:-2]
print(len(s))
