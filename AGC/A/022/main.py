s = input()

print(s)

# こういう複雑なものは、再帰的な実装ができないか考える
# s = input()
# *alp, = map(chr, range(97, 123))
# c = set(s)
# if len(c) != 26:
#     x = sorted(set(alp) - c)[0]
#     print(s+x)
# else:
#     z_idx = s.index("z")
#     last_idx = z_idx
#     cnt = 0
#     for j in range(26-z_idx):
#         if s[z_idx+j] == alp[::-1][j]:
#             last_idx = z_idx+j
#             cnt += 1
#             continue
#         break

#     if cnt == 26:
#         print(-1)
#     elif last_idx == 25:
#         next_idx = alp.index(s[z_idx-1])+1
#         print(s[:z_idx-1]+alp[next_idx])
#     else:
#         ans = s[:last_idx+1]
#         tmp = list(s[last_idx+1:])
#         loop = len(tmp)-1
#         prev = "a"
#         for i in range(loop):
#             a, b, *c = tmp[::-1]
#             if prev > b:
#                 tmp.pop()
#                 tp = tmp.pop()
#                 tmp.append(prev)
#                 prev = tp
#                 continue
#             elif a > b:
#                 tmp.pop()
#                 prev = tmp.pop()
#                 tmp.append(a)
#                 # ans += "".join(c[::-1])+a
#                 continue
#             else:
#                 tmp.pop()
#                 continue
#         print(ans+tmp[0])
