__author__ = 'student'
A = [1, 2, 3, 4, 5]
for i in range(len(A)//2 + len(A)%2):
    print(A[i], end=' ')
    if A[i] != A[-i-1]:
        print(A[-i-1], end=' ')
