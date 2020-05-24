s = input()
if all(c in '0123456789' for c in s):
    print(2*int(s))
else:
    print('error')
