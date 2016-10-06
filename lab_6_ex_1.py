__author__ = 'student'
import random
import matplotlib.pyplot as plt

random.seed(0)
plt.subplot(221)
N = 100
values = [random.normalvariate(0, 1) for i in range(N)]
plt.hist(values, bins=100)

random.seed(0)
plt.subplot(222)
N = 1000
values = [random.normalvariate(0, 1) for i in range(N)]
plt.hist(values, bins=100)

random.seed(0)
plt.subplot(223)
N = 10000
values = [random.normalvariate(0, 1) for i in range(N)]
plt.hist(values, bins=100)

random.seed(0)
plt.subplot(224)
N = 100000
values = [random.normalvariate(0, 1) for i in range(N)]
plt.hist(values, bins=100)
plt.show()