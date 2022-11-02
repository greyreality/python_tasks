#http://pythontutor.ru/visualizer/
# Write a function:def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0)
# that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Assume that:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Complexity:
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# сложность O(N**2) -> missingint
def solution(A):
    A = sorted(A) #use timsort complexity n*log(n)
    print(A)
    if A[len(A) - 1] > 0:
        start = int(A[len(A) - 1])
    else:
        return 1

    for i in range(1, start):
       # print('i=', i)
        if i not in A:
            return i
    else:
        if start !=0:
            return start + 1
A = [1, 3, 6, 4, 1, 2]
print(solution(A))
A = [1,2,3,4,5,6,7,8,9,10,99999,100000]
print(solution(A))
A = [1000000000]
print(solution(A))
A = [1, 3, 2]
print(solution(A))
