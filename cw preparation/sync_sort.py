a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(len(a)-1):
    for k in range(i+1, len(a)):
        if a[i] > a[k]:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
        elif a[i] == a[k]:
            if b[i] > b[k]:
                b[i], b[k] = b[k], b[i]
print(*a, '\n', *b)