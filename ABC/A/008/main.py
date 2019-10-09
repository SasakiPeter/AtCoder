s, t = map(int, input().split())
print(t-s+1)


# これはビット演算使えてるってあんまり言わない？
# print(-~(t-s))

# これはどうか？
# print(~(s-t)+2)
# print(~eval(input().replace(' ', '-'))+2)
