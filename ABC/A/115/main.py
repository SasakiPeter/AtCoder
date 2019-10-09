d = int(input())
# c = 'Christmas'
# e = 'Eve'
# print(c if d == 25 else ' '.join([c, e]) if d == 24 else ' '.join(
#     [c, e, e]) if d == 23 else ' '.join([c, e, e, e]))

# print(' '.join(['Christmas']+['Eve']*(25-d)))
# print(*(['Christmas']+['Eve']*(25-d)))

# わざわざリストにする必要すらない
print('Christmas'+' Eve'*(25-d))
