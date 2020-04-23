import itertools
a, *bcd = input()
for operater in itertools.product(['+', '-'], repeat=3):
    formula = a
    formula += "".join(op+num for op, num in zip(operater, bcd))
    if eval(formula) == 7:
        print(formula+'=7')
        break
