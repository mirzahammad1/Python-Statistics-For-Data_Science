def matrix_addition(x,y):
    xrows = len(x)
    xcols = len(x[0])
    yrows = len(y)
    ycols = len(y[0])
    if xrows != yrows or xcols != ycols:
        print("Sum is not defined as the matrices have different orders")
    else:
        z=x 
        for i in range (xrows):
            for j in range (xcols):
                z[i][j]= z[i][j] + y[i][j]
        return z

print(matrix_addition([[1,2,5],[3,4,1]],[[5,1,2],[9,3,4]]))