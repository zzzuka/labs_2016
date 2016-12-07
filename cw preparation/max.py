a = int(input())
num = 1
k = 0
max_a = a
mas = []
while a != 0:
    a = int(input())
    k += 1
    if a == max_a:
        num += 1
        mas.append(k)
    elif a > max_a:
        num = 1
        max_a = a
        mas = [k]
print('Количество максимумов', num, '\n Положение максимумов', ''.join(mas))
