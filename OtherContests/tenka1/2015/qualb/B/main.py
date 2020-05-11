s = input()
ans = ''
x = 'set'
bracket_depth = 0
for c in s:
    if c == '{':
        bracket_depth += 1

    elif c == '}':
        bracket_depth -= 1
        if bracket_depth == 0:
            ans = x

    elif bracket_depth == 1:
        if c == ':':
            x = 'dict'

print('dict' if s == '{}' else ans)
