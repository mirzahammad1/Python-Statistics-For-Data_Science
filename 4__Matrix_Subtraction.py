def matrix_subtraction(x,y):
    xrows = len(x)
    xcols = len(x[0])
    yrows = len(y)
    ycols = len(y[0])
    if xrows != yrows or xcols != ycols:
        print("Difference is not defined as the matrices have different orders")
    else:
        z=x 
        for i in range (xrows):
            for j in range (xcols):
                z[i][j]= z[i][j] - y[i][j]
        return z

print(matrix_subtraction([[5,4,3],[3,4,-9]],[[5,3,2],[8,2,4]]))