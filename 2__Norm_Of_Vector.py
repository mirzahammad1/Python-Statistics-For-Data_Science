import math
def norm_vector(v):
    dot_product = sum(i*i for i in v)
    return math.sqrt(dot_product)

print(norm_vector([-1,-2,3,4,5]))