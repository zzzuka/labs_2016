__author__ = 'student'
A = [1, 2, 3, 4, 2]
k = 2
for i in range(k):
    A.insert(-1-A[-1], A[-1])
    A.pop()
print(*A)