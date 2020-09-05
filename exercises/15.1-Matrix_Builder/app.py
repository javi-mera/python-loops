import random

entero=random.randint(2, 4)
row=[]
matrix=[]
def matrixBuilder(entero):
    for i in range(entero):
       row.append(1)
    for i in range(entero):
        matrix.append(row)
    return matrix
print(matrixBuilder(entero))

