# 文字列がそんなに大きくならないので、適当にシミュレーションする
s = input()


def rec(s):
    start = end = None
    # 括弧の始まりと終わりを見つけたい
    for i in range(len(s)):
        # (→)の順番に出てくる区間が欲しい
        if s[i] == '(':
            start = i
        elif s[i] == ')':
            end = i
            break
    if start is None:
        return s
    new_s = s[:start]+s[start+1:end]+s[start+1:end][::-1]+s[end+1:]
    return rec(new_s)


print(rec(s))
