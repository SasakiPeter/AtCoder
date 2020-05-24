s = input()
words = []
word = ''
start = 0
for c in s:
    if c.isupper():
        start ^= 1
        if start:
            word = c
        else:
            word += c
            words.append(word)
    else:
        word += c
words.sort(key=lambda x: x.lower())
print("".join(words))
