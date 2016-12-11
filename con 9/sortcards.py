m = ['c', 's', 'h', 'd']
d = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
n = int(input())
s = input()
cards = [''] * n
for i in range(len(s)):
    if s[i] in d and i % 2 == 0:
        cards[i // 2] += s[i:i+2]
for k in range(len(cards) - 1):
    for i in range(len(cards) - 1):
        if m.index(cards[i][1]) > m.index(cards[i+1][1]):
            cards[i], cards[i+1] = cards[i+1], cards[i]
for k in range(len(cards) - 1):
    for i in range(len(cards) - 1):
        if d.index(cards[i][0]) > d.index(cards[i+1][0]):
            cards[i], cards[i+1] = cards[i+1], cards[i]
print(''.join(cards))