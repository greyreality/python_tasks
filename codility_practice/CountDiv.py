# def solution(A, B, K)
# that, given three integers A, B and K, returns the number of integers within the range [A..B]
# that are divisible by K, i.e.:
# { i : A ≤ i ≤ B, i mod K = 0 }
# For example, for A = 6, B = 11 and K = 2, your function should return 3,
# because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
# Assume that:
# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.
# Complexity:
# expected worst-case time complexity is O(1);
# expected worst-case space complexity is O(1).
# correctnes 100%
# complexity: O(1)
#  38min
def solution(A, B, K):
    if A == B == K:
        return 1
    elif K > A and K > B and A ==0:
        return 1
    elif K > A and K > B and A !=0:
        return 0
    elif A == B and K < A:
        if A % K == 0:
            return 1
        else: return 0

    for i in range(A, B + 1):
        if i % K == 0:
            print('i=', i)
            break
    for j in range(B, A + 1, -1):
        if j % K == 0:
            print('j=', j)
            break
    print('start=', i / K)
    start = int(i / K)
    print('end=', j / K)
    end = int(j / K)
    return end - start + 1


print('answer=', solution(5, 5, 4))
