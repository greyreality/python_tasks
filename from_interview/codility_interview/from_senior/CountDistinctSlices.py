# An integer M and a non-empty zero-indexed array A consisting of N non-negative integers are given.
# All integers in array A are less than or equal to M.
# A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A.
# The slice consists of the elements A[P], A[P + 1], ..., A[Q].
# A distinct slice is a slice consisting of only unique numbers. That is, no individual number occurs more than once in the slice.
# For example, consider integer M = 6 and array A such that:
# [3,4,5,5,2]
#     A[0] = 3
#     A[1] = 4
#     A[2] = 5
#     A[3] = 5
#     A[4] = 2
# There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).
# The goal is to calculate the number of distinct slices.
# Write a function:def solution(M, A)
# that, given an integer M and a non-empty zero-indexed array A consisting of N integers, returns the number of distinct slices.
# If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.
# For example, given integer M = 6 and array A such that: [3,4,5,5,2]
# the function should return 9, as explained above.
# Assume that:
# N is an integer within the range [1..100,000];
# M is an integer within the range [0..100,000];
# each element of array A is an integer within the range [0..M].
# Complexity:
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(M), beyond input storage (not counting the storage required for input arguments).
# Detected time complexity:O(N)
# correctness 100%
def solution(M, A):
    accessed = [-1] * (M + 1)  # -1: not accessed before
    # Non-negative: the previous occurrence position
    front, back = 0, 0
    result = 0

    for front in range(len(A)):
        if accessed[A[front]] == -1:
            # Met with a new unique item
            accessed[A[front]] = front
        else:
            # Met with a duplicate item
            # Compute the number of distinct slices between newBack-1 and back
            # position.
            newBack = accessed[A[front]] + 1
            result += (newBack - back) * (front - back + front - newBack + 1) / 2
            if result >= 1000000000:   return 1000000000

            # Restore and set the accessed array
            for index in range(back, newBack):
                accessed[A[index]] = -1
            accessed[A[front]] = front

            back = newBack

    # Process the last slices
    result += (front - back + 1) * (front - back + 2) / 2

    return int(min(result, 1000000000))

s = [3,4,5,5,2]
print(solution(6,s))