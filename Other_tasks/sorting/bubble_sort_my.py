def bubble_sort(a):
    n = len(a)
    q = 0
    print('len= ', n, 'array=', a)
    for i in range(0, n - 1):  # 8times
        for j in range(0, n - 1):  # 8times
            q += 1
            if a[j] > a[j + 1]:
                left = a[j]
                right = a[j + 1]
                a[j] = right
                a[j + 1] = left
            print('q=', q, 'array = ', a)
        # print('q=', q, 'array = ', a) # по четыре раза в цикле мелком прошли
        q = 0
        s = 0
        # for i in range(n - 1, 0, -1):  # 4 3 2 1 0
        #     for j in range(0, i):  # 3
        #         s += 1
        #         if a[j] > a[j + 1]:
        #             left = a[j]
        #             right = a[j + 1]
        #             a[j] = right
        #             a[j + 1] = left
        #     print('s=', s, 'array = ', a)
        #     s = 0
        # print('final\t', a)  # 64 times
    return a

a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("result=", bubble_sort(a))