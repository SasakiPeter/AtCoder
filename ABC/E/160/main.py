x, y, a, b, c = map(int, input().split())
p = sorted(map(int, input().split()), reverse=True)[:x]
q = sorted(map(int, input().split()), reverse=True)[:y]
r = list(map(int, input().split()))
ls = sorted(p+q+r, reverse=True)[:x+y]
print(sum(ls))
