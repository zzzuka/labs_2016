def decomp(n):
    q = [[0] * (n + 1) for i in range(n + 1)]

    for i in range(0, n + 1):
        q[0][i] = 1

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            for k in range(1, j + 1):
                q[i][j] += q[i - k][k]
        for j in range(i + 1, n + 1):
            q[i][j] = q[i][i]
    return q[n][n]

n = int(input())
print(decomp(n))

