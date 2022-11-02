# A Python program to print all
# combinations of given length
from itertools import combinations

# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3,4,5], 2)
print('comb=',type(comb))
# Print the obtained combinations
lst = list(comb)
for i in list(comb):
    print('i=',i)
print('lst=',lst)
