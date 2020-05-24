n = int(input())
d1 = n % 10
if str(d1) in '24579':
    print('hon')
elif d1 == 3:
    print('bon')
else:
    print('pon')
