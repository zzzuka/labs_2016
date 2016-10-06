__author__ = 'student'
n = int(input())

k = [i**2 if (i) % 3 == 1 else 0 for i in range(n)]
print(sum(k))