def scalar_multiplication(c,x):
    cx = x
    for i in range(len(x)):
        for j in range (len(x[0])):
            cx[i][j] = c*cx[i][j]
            return cx
        
print(scalar_multiplication(-3,[[2,6,-1],[2,8,0],[9,8,7]]))