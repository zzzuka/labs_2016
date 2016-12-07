def define(o):
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    o -= 10
    return s[o]
#r = input()
#a = list(r.split(' '))
n = int(input())
A = int(input(), base=n)
k = int(input())

s = ''
while A != 0:
    o = A % k
    if o >= 10:
        o = define(o)
    s = str(o) + s
    A //= k
print(s)
