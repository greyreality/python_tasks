# We draw N discs on a plane. The discs are numbered from 0 to N − 1. A zero-indexed array A of N non-negative integers,
# specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].
# We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point
# (assuming that the discs contain their borders).
# The figure below shows discs drawn for N = 6 and A as follows:
#   A[0] = 1  A[1] = 5   A[2] = 2   A[3] = 1  A[4] = 4  A[5] = 0
# There are eleven (unordered) pairs of discs that intersect, namely:
# discs 1 and 4 intersect, and both intersect with all the other discs;
# disc 2 also intersects with discs 0 and 3.
# Write a function: def solution(A)
# that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs.
# The function should return −1 if the number of intersecting pairs exceeds 10,000,000.
# Given array A shown above, the function should return 11, as explained above.
# Assume that:
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [0..2,147,483,647].
# Complexity:
# expected worst-case time complexity is O(N*log(N));
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# correctnes 100%

def solution(A):
    counter = 0
    N = len(A)
    stop_intersecting = [0] * N
    for i in range(0, N):
        r = A[i]
        intersect_with = i if i - r < 0 else  i - stop_intersecting[i - r]
        counter += intersect_with
        if (counter > 10000000): return -1
        stop_intersecting_at = i + r + 1
        if stop_intersecting_at < N: stop_intersecting[stop_intersecting_at] += 1
        iNext = i + 1
        if iNext < N: stop_intersecting[iNext] += stop_intersecting[i]
    return counter


n = 100000
min = 0
max = 10
w = [n]
# for p in range(n):
#     w.append(random.randint(min, max))
# print(w)
# print('res=', solution(w))
test = [1, 5, 2, 1, 4, 0]
print('res=', solution(test))
