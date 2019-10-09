s = input()
even = 'RUD'
odd = 'LUD'
print('Yes' if all(c in even for c in s[::2]) and all(
    c in odd for c in s[1::2]) else 'No')
