def insert_sort(a):
    n = len(a)
    print('len= ', n, '\narray=', a)
    for i in range(1, n):
        j = i
        # print('j=', j, ' array=', a)
        while j > 0 and a[j] < a[j - 1]:
            left = a[j - 1]
            right = a[j]
            a[j - 1] = right
            a[j] = left
            j = j - 1
            #      print('here array=', a)
    return a

a = [54, 26, 93,4,0,1,2,10,3,5,89,7]
insert_sort(a)
print('result = ',a)