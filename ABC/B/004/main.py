# m = [input()[::-1] for _ in range(4)][::-1]
# print(*(row for row in m), sep='\n')

# もっと簡単に書ける
# for row in [input()[::-1] for _ in range(4)][::-1]:
#     print(row)

# strとして扱えば、一度の反転で十分
print('\n'.join(input() for _ in range(4))[::-1])
