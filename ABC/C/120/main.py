# s = input()
# cnt_zero = s.count('0')
# cnt_one = len(s) - cnt_zero
# print(min(cnt_one, cnt_zero)*2)

# stackの練習
# 前から貪欲にstackする場合
s = input()
stack = []
for c in s:
    if not stack:
        stack.append(c)
    elif c != stack[-1]:
        stack.pop()
    else:
        stack.append(c)
print(len(s)-len(stack))
