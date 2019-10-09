w, h = map(int, input().split())
# 0 and 0 -> 0: False and False -> False
# 0 and 1 -> 0: False and True -> Flase
# 0 or 0 -> 0: False or False -> False
# 0 or 1 -> 1: False or True -> True

# or は Flaseに対して厳しくなる
# and は Trueに対して厳しくなる
print('4:3' if w % 16 or h % 9 else '16:9')
# print('16:9' if w % 16 == 0 and h % 9 == 0 else '4:3')

# まとめた方がいい感じ
# print('4:3' if w*h % 144 else '16:9')
