
import numpy as np
import statistics 
x = np.array([2,3,4,5,6,7,8,9,1,13])
y = np.array([11,12,13,14,15,16,17,18,19,22])
stx = statistics.stdev([2,3,4,5,6,7,8,9,1,13])
sty = statistics.stdev([11,12,13,14,15,16,17,18,19,22])



# Covariance gives the direction of the linear relationship

meanx = sum(x)/float(len(x))
meany = sum(y)/float(len(y))
xpart = [i - meanx for i in x]
ypart = [i - meany for i in y]
numerator = sum([xpart[i] * ypart[i] for i in range (len(xpart))])
denominator = len(x) - 1
covariance = numerator / denominator
print(covariance)

# Correlation gives both dirction and strength
# correlation is function of covariance

correlation = covariance / (stx * sty)
print(correlation)