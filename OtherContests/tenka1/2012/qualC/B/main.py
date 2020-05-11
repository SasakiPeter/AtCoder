s = input()
marks = ['S', 'H', 'D', 'C']
for m in marks:
    s = s.replace(m, ' '+m)
deck = s.split()

rsf = ['10', 'J', 'Q', 'K', 'A']
cards = [[0]*5 for _ in range(4)]
for cnt, card in enumerate(deck):
    mark, num = card[0], card[1:]
    if num in rsf:
        cards[marks.index(mark)][rsf.index(num)] = 1
        if sum(cards[marks.index(mark)]) == 5:
            break

# markで揃うことがわかった cnt+1枚
trash = ''
for card in deck[:cnt+1]:
    m, num = card[0], card[1:]
    if m == mark and num in rsf:
        continue
    trash += card
print(trash if trash else 0)
