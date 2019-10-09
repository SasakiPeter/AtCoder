# for
n = int(input())
s = input()
x = ans = 0
for c in s:
    x += [-1, 1][c == 'I']
    ans += (ans < x)+0
    # ans = [ans, x][ans < x]
print(ans)
