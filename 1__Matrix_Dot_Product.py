def dot_product(x,y):
    return sum(i*j for i,j in zip(x,y,strict=True))

print (dot_product([3,4,6],[1,7,-2]))