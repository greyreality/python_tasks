def report():
    # A = [1,1,1,1,10]
    A = [2, 2, 2, 2, 2, 3, 4, 147, 483]
    n = len(A) #length of array
    print('n=', n)
    print('n/2=',n/2)
    L = [-1] + A # add to array first value
    print('L=', L)
    count = 0
    pos = (n + 1) // 2 #middle of array
    print('pos=', pos)
    candidate = L[pos] #value of a middle of array
    print('candidate=', candidate)
    for i in range(1, n + 1):
     #   print(i,'array = ', L[i])
        if (L[i] == candidate):
            count = count + 1
            print(i,' count=', count)
   # if (count > pos):
    if (count > (n/2)):
        return print('candidate end=',candidate) # contains a leader
    return print('-1')  # A does not contain a leader

report()
