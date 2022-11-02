# def solution(A)
# that, given a zero-indexed array A consisting of N integers,
# returns the number of distinct уникальные values in array A.
# Assume that:
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# For example, given array A consisting of six elements such that:
#  A[0] = 2    A[1] = 1    A[2] = 1  A[3] = 2    A[4] = 3    A[5] = 1
# the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.
# Complexity:
# expected worst-case time complexity is O(N*log(N));
# expected worst-case space complexity is O(N),
# beyond input storage (not counting the storage required for input arguments)
# Detected time complexity: O(N*log(N)) or O(N)
# correctnes 100%
# 10min
import random
def solution(A):
    if not A:
        return 0
    return len(set(A))

n = 100000
min = -1000000
max =  1000000

a=[n]
for x in range(n):
    a.append(random.randint(min,max))
print(a)
print('num=',solution(a))
b = []
print('zero_num=',solution(b))