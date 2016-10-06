__author__ = 'student'
A = [1, 2, 3, 4, 5]

i = 0
while i < len(A):
    A[i], A[i+1] = A[i+1], A[i]
    i += 2
print(A)



A.insert(0, A[len(A)])
A.pop()
print(A)



for i in A:
    if A.count(A[i]) == 1:
        print(A[i])



m = 0
for i in A:
    if A.count(A[i]) > m:
        m = A.count(A[i])
print(m)




