#python 3
# A non-empty array A consisting of N integers is given.
# The first covering prefix of array A is the smallest integer P
# such that 0≤P<N and such that every value that occurs in array A
# also occurs in sequence A[0], A[1], ..., A[P].
# For example, the first covering prefix of the following 5−element array A:
#   A[0] = 2
#   A[1] = 2
#   A[2] = 1
#   A[3] = 0
#   A[4] = 1
# is 3, because sequence [ A[0], A[1], A[2], A[3] ] equal to [2, 2, 1, 0],
# contains all values that occur in array A.
# Write a function: def solution(A)
# that, given a non-empty array A consisting of N integers, returns the first covering prefix of A.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..1,000,000];
# each element of array A is an integer within the range [0..N−1].

#Detected time complexity: O(N**3)
def solution(A):
    unique_values = []
    ind = []
    for i in A:
        if i not in unique_values:
            unique_values.append(i)

    for i in unique_values:
        for j in A:
            if i == j:
                ind.append(A.index(j))
                break
    return  (int(max(ind)))

A =[2,2,1,0,1]
print(solution(A))