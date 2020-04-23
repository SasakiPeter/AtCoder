import itertools
s = input()
ans = 0
for plus in itertools.product(['', '+'], repeat=len(s)-1):
    formula = s[0]
    formula += "".join([op+num for op, num in zip(plus, s[1:])])
    ans += eval(formula)
print(ans)
