# An array A consisting of N integers is given. An inversion is a pair of indexes (P, Q) such that P < Q and A[Q] < A[P].
#
# Write a function:
#
# def solution(A)
#
# that computes the number of inversions in A, or returns −1 if it exceeds 1,000,000,000.
#
# Assume that:
#
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
# For example, in the following array:
# [-1,6,3,4,7,4]
#  A[0] = -1 A[1] = 6 A[2] = 3
#  A[3] =  4 A[4] = 7 A[5] = 4
# there are four inversions:
#
#    (1,2)  (1,3)  (1,5)  (4,5)
# so the function should return 4.
#
# Complexity:
#
# expected worst-case time complexity is O(N*log(N));
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# Detected time complexity:O(N*log(N))
# correctness 100%

import bisect

def solution(A):
    # computes the number of inversions in A, or returns -1 if it exceeds 1,000,000,000
    # the idea is to store elements left of n-th sorted,
    # which would allow us to easily find the number of them greater than n-th.
    sorted_left = []
    res = 0
    for i in range(1, len(A)):
        bisect.insort_left(sorted_left, A[i-1])
        # i is also the length of sorted_left
        res += (i - bisect.bisect(sorted_left, A[i]))
        if res > 1000000000:
            return -1
    return res

s = [-1,6,3,4,7,4]
print(solution(s)) # 4
