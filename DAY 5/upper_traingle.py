matrix =[1, 2, 3,
        4, 5, 6,
        7, 8, 9]
row = int(input())
column = int(input())
for i in range(row):
    for j in range(column):
        if i < j:
            print("0", end=" ")
        else:
            print(matrix[i][j], end=" ")
    print() 
