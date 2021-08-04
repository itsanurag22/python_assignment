mat = []
for i in range(0, 5):
    mat.append([])
    mat[i] = list(map(int,input().split()))
    for j in range(0, 5):
        if(int(mat[i][j]) == 1):
            temp_i = i
            temp_j = j


print(abs(temp_i - 2) + abs(temp_j - 2))