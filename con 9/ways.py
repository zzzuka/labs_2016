def wn(n, m):
    k = [[0]*(m+2) for i in range(n+2)]
    k[1][1:] = [1]*(m+1)
    for i in range(2, n+2):
        for j in range(1, m+2):
            k[i][j] = k[i][j-1] + k[i-1][j]
    return k[n][m]

a = list(map(int, input().split(' ')))
n, m = a[0], a[1]
print(wn(n+1,m+1))