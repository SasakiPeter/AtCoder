# imos+座圧
n = int(input())
needs = []
for _ in range(n):
    a, b = map(int, input().split())
    needs.append((a, 1))
    needs.append((b+1, -1))
needs.sort()
# 集計
ans = cnt = 0
for c, v in needs:
    cnt += v
    ans = max(ans, cnt)
print(ans)

# # imos
# n = int(input())
# MAX_C = 10**6
# c = [0]*(MAX_C+2)
# for _ in range(n):
#     a, b = map(int, input().split())
#     c[a] += 1
#     c[b+1] -= 1

# # 集計
# ans = 0
# for i in range(MAX_C+1):
#     c[i+1] = c[i]+c[i+1]
#     ans = max(ans, c[i])
# print(ans)
