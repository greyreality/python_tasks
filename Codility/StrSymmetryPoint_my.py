# Write a function: def solution(S)
# that, given a string S, returns the index (counting from 0) of a character such that the part of the string to the left of that character
# is a reversal of the part of the string to its right. The function should return −1 if no such index exists.
# Note: reversing an empty string (i.e. a string whose length is zero) gives an empty string.
# For example, given a string: "racecar"
# the function should return 3, because the substring to the left of the character "e" at index 3 is "rac", and the one to the right is "car".
# Given a string:"x"
# the function should return 0, because both substrings are empty.
# Assume that:
# the length of S is within the range [0..2,000,000].
# Complexity:
# expected worst-case time complexity is O(length(S));
# expected worst-case space complexity is O(1) (not counting the storage required for input arguments).
# Detected time complexity:O(length(S))
# correctness 100%
def solution(S):
    sLen = len(S)
    # Symmetry point is possible, when and only when the string's length is odd.
    if sLen % 2 == 0:   return -1
    # With a odd-length string, the only possible symmetry point is the middle point.
    mid = sLen // 2
    begin = 0
    end = sLen - 1
    # The middle point of an odd-length string is symmetr point, only when the string is symmetry.
    while begin < mid:
        if S[begin] != S[end]:      return -1
        begin += 1
        end -= 1
    return mid

s = 'racecar'
print(solution(s))
