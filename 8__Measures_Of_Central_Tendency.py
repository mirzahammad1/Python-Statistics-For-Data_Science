
import statistics
## Measures Of Central Tendency consists of 3 types

### for finding Mean
a = [4,89,54,-7,-9,27,5]
print(statistics.mean(a))

### for median
b = [1,2,3,4,5,6,7,8,9,10]
print(statistics.median(b))

### for mode 

set1 =[1, 2, 3, 3, 4, 4, 4, 5, 5, 6]
# In the given data-set
# Count of 1 is 1
# Count of 2 is 1
# Count of 3 is 2
# Count of 4 is 3
# Count of 5 is 2
# Count of 6 is 1
# We can infer that 4 has the highest population distribution
# So mode of set1 is 4
print(statistics.mode(set1))