from collections import Counter
n, m = map(int, input().split())
name_c = Counter(input())
kit_c = Counter(input())
ans = 0
for k, v in name_c.items():
    if kit_c[k] == 0:
        ans = -1
        break
    ans = max(ans, -(-v//kit_c[k]))
print(ans)


# # test
# if ans == -1:
#     # for k, v in name_c.items():
#     pass

# else:
#     for k, v in name_c.items():
#         assert v <= kit_c[k]*ans
