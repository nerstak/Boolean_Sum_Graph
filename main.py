import functions

size=int(input("Number of elements in the matrix: "))

matrix=[[[0 for x in range(size)] for y in range(size)] for z in range(1)]


for i in range(size):
    for j in range(size):
        matrix[0][i][j]=int(input("Link from "+str(i+1)+" to "+str(j+1)+"? "))

for i in range(size):
    for j in range(size):
        print(matrix[0][i][j],end=" ")
    print("")

step=int(input("How many step do you want to check? "))
for i in range(step-1):
    functions.power_mat(matrix,size)
result_treated = functions.boolean_sum(functions.sum_mat(matrix,size),size)

for i in range(size):
    for j in range(size):
        print(result_treated[i][j],end=" ")
    print("")
