s = input()
n = len(s)


def hash(s):
    return sum(map(lambda x: ord(x)-96, s))


def check(s, t):
    if hash(s) == hash(t) and 1 <= len(t) <= 20 and s != t:
        return True
    else:
        return False


ans = s[1:]+s[0]
if check(s, ans):
    print(ans)
else:
    # 全部同じ時だめ
    unique = s[0]
    if unique != 'a':
        ans = chr(ord(unique)-1)
    else:
        ans = chr(ord(unique)+1)

    h = hash(s)-hash(ans)

    while 0 < h:
        ans += chr(96+min(h, 26))
        h -= min(h, 26)
    if check(s, ans):
        print(ans)
    else:
        print('NO')
