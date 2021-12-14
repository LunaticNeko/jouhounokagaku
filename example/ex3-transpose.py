m = 3
n = 2
A = [[1,2],[3,4],[5,6]]

AT = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        AT[i][j] = A[j][i]

print(AT)
