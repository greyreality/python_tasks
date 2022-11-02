def bubble_sort(a):
    length = len(a)
    # print('len=',length)
    for i in range(length - 1, 0, -1):
        for j in range(0, i):
            print('i=',i, 'j=',j)
            print('compare', a[j],  "and", a[j + 1])
            # print('compare', a[j], "[",j,"]", "and", a[j+1],"[",j+1,"]")
            if a[j] > a[j + 1]:

                left = a[j]
                right = a[j + 1]
                a[j] = right
                a[j + 1] = left
                print("after switch=",a)
    return a

a = [54,93,4,0,1]
print("before = ",a)
bubble_sort(a)
print('after = ',a)