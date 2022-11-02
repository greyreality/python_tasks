# Detected time complexity: O(N)
# correctness 100%
# hz kak sdelal
def solution(A):
    n = len(A)
    if n == 0:
        return -1
    elif n == 1:
        return 0
    stack = []
    stack.append(A[0])
    size = 1
    for i in range(1, n):
        if (size > 0) and (stack[-1] != A[i]):
            # print('stack[-1]', stack[-1], 'a[i]',A[i])
            stack.pop() #del last
            size -= 1
        else:
            stack.append(A[i])
            size += 1
    print('stack',stack)

    if (size > 0):
        candidate = stack.pop()
    else:
        return -1

    count = 0
    for i in range(n):
        if A[i] == candidate:
            pos = i
            count += 1

    if (count * 2 > n):
        return pos
    else:
        return -1


test = [4, 8, 8, 8, 1,1]
print('res=', solution(test))
