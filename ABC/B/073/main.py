# n = int(input())
# ans = 0
# for _ in range(n):
#     l, r = map(int, input().split())
#     ans += r-l+1
# print(ans)

# この方がスッキリ
n = int(input())
print(sum(1-eval(input().replace(' ', '-')) for _ in range(n)))

# eval使うなんてすごい力技
