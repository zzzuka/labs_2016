n = int(input())
s = []
keys = []
for i in range(n):
    key = input()
    s.append(key)
    if key not in keys:
        keys.append(key)
values = []
for key in keys:
    values.append(s.count(key))
products = dict(zip(keys, values))
max_value = 0
sub_max_value = 0
for key in products:
    if products[key] > max_value:
        sub_max_value = max_value
        max_value = products[key]
    if max_value > products[key] > sub_max_value:
        sub_max_value = products[key]
print('Количество самых популярных товаров =', max_value, '\nКоличество вторых по популярности', sub_max_value)
