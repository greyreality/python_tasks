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
    discs_count = len(A)  # The total number of discs
    range_upper = [0] * discs_count  # The upper limit position of discs
    range_lower = [0] * discs_count  # The lower limit position of discs

    # Fill the limit_upper and limit_lower
    for index in range(0, discs_count):
        range_upper[index] = index + A[index]
        range_lower[index] = index - A[index]

    range_upper.sort()
    range_lower.sort()

    range_lower_index = 0
    intersect_count = 0
    for range_upper_index in range(0, discs_count):
        # Compute for each disc
        while range_lower_index < discs_count and range_upper[range_upper_index] >= range_lower[range_lower_index]:
            # Find all the discs that:
            #    disc_center - disc_radius <= current_center + current_radius
            range_lower_index += 1
        # We must exclude some discs such that:
        #    disc_center - disc_radius <= current_center + current_radius
        #    AND
        #    disc_center + disc_radius <(=) current_center + current_radius
        # These discs are not intersected with current disc, and below the
        #    current one completely.
        # After removing, the left discs are intersected with current disc,
        #    and above the current one.
        # Attention: the current disc is intersecting itself in this result
        #    set. But it should not be. So we need to minus one to fix it.
        intersect_count += range_lower_index - range_upper_index - 1
        if intersect_count > 10000000:
            return -1

    return intersect_count


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
