__author__ = 'student'
k = int(input())
n = int(input())
A = []

# for i in range(n+1):
#     A.append(1)
A=[1]*(n)
for i in range(k, n+1):
    A[i] = (sum(A[i-k:i]))
print(A[-1])
