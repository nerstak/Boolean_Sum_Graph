def power_mat(matrix, size):
    result=[[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] = result[i][j] + matrix[0][i][k] * matrix[len(matrix)-1][k][j]
    matrix.append(result)

def sum_mat(matrix,size):
    result=[[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(len(matrix)):
                result[i][j]=result[i][j]+matrix[k][i][j]
    return result

def boolean_sum(matrix,size):
    result=[[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(size):
            if matrix[i][j]!=0:
                result[i][j]=1
    return result