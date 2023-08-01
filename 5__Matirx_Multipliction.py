def matrix_multiplication(x,y):
    xrows = len(x)
    xcols = len(x[0])
    yrows = len(y)
    ycols = len(y[0])
    if xcols != yrows:
        print("Product is not defined")
    else:
        z=[[0 for i in range (ycols)] for j in range (xrows)]
        for i in range (xrows):
            for j in range (ycols):
                total = 0
                for ii in range (xcols):
                    total += x[i][ii] * y[ii][j]
                    z [i][j] = total
        return z

print (matrix_multiplication([[1,2,5],[3,4,1]],[[5,1,2],[9,3,4],[1,5,3]]))