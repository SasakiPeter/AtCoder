ans = 0
for _ in range(3):
    s, e = map(int, input().split())
    ans += s*e//10
print(ans)

# print(sum(eval(input().replace(' ', '*')) for _ in range(3))//10)
