import numpy as np
import random
import matplotlib.pyplot as plt

#1
def get_percentile(values, bucket_number):
        k = 100/bucket_number
        res = []
        ch = 0
        for _ in range(bucket_number):
            res.append(np.percentile(values, ch))
            ch += k
        res[0] = 0.0
        return res
"""
values = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
print(get_percentile(values, 4))
"""

#2
def get_percentile_number(value, percentiles):
    i =0
    while percentiles[i] <= value:
        index = i
        if i < len(percentiles) - 1:
            i += 1
        else:
            break
    return index

"""
values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
percentiles = get_percentile(values, 4)
print(percentiles)
print(get_percentile_number(2.5, percentiles))
print(get_percentile_number(5.5, percentiles))
print(get_percentile_number(100, percentiles))
"""

#3 4
def value_equalization(value, percentiles, add_random = False):
    step = 1/len(percentiles)
    idx = get_percentile_number(value, percentiles)
    new_value = idx*step
    if add_random is True:
        random_noise = random.uniform(0, step)
        new_value = idx*step + random_noise
    return new_value

"""
values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
percentiles = get_percentile(values, 5)
print(percentiles)
print(value_equalization(5.5, percentiles))
print(value_equalization(5.5, percentiles))
print(value_equalization(5.5, percentiles))

"""
#5
def values_equalization(values, percentiles, add_random = False):
    for i in range(len(values)):
        values[i] = value_equalization(values[i], percentiles, add_random)
    return values

"""
values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
percentiles = get_percentile(values, 5)
print(percentiles)
print(values_equalization(values, percentiles, add_random=False))
print(values_equalization(values, percentiles, add_random=True))
print(values_equalization(values, percentiles, add_random=True))
"""

#6

data = []
with open ('img.txt', 'r') as f:
    for line in f:
        v = list(map(float, line.strip().split()))
        data.append(v)

data = np.array(data)

#7
plt.subplot(221)
plt.imshow(data, cmap = plt.get_cmap('gray'))
plt.title(r'$Before$')


#8
plt.subplot(222)
N = 100
values = [data.flatten()]
plt.hist(values, bins=100)
plt.title(r'$Image hist before visualisation$')

percentiles = get_percentile(values, 5)
new_data = values_equalization(data.flatten(), percentiles, add_random = True)
final = new_data.reshape(200,267)

#9
plt.subplot(223)
plt.imshow(final, cmap = plt.get_cmap('gray'))
plt.title(r'$After$')

#10
plt.subplot(224)
N = 100
values = [final]
plt.hist(values, bins=100)
plt.title(r'$Image hist after equalization$')
plt.show()

#12
new_data = []
for i in range (100):
    new_data.append(random.choice(data))
plt.imshow(new_data, cmap = plt.get_cmap('pink'))
plt.show()

#13
number_data = []
new_data = []
n = [i for i in range(200)]
number_data = random.sample(n,100)
for i in range (100):
    new_data.append(data[number_data[i]])
plt.imshow(new_data, cmap = plt.get_cmap('pink'))
plt.show()