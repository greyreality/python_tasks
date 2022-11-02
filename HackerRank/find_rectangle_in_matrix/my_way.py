import numpy as np

def findcorner(i,j,a,firstcoordinate,index):
    print("a[", i, "][", j, "]=", a[i][j])
    x = len(a)
    y = len(a[0])
    print("x=",x,"y=",y)
    for m in range (i,x):
        if a[m][j]==1:
            print("firstcoordinate with index=",firstcoordinate[index])
            # firstcoordinate = np.append(firstcoordinate, [[i, j]], axis=0)
            firstcoordinate[index] = [firstcoordinate[index,0],firstcoordinate[index,1],a[m][j]]
            print("firstcoordinate ==",firstcoordinate)
            break
        if a[m][j]==5:
            pass




def get_rectangle_coordinates(a,index):
    x = len(a)
    y = len(a[0])
    # print("x=",x,"y=",y)
    firstcoordinate = np.empty(shape=[0, 3])
    index = -1
    # print("first value=",firstcoordinate)
    for i in range(0,x):
        for j in range(0,y):
            if a[i][j]==0:
                # print("a[",i,"][",j,"]=",a[i][j])
                firstcoordinate = np.append(firstcoordinate,[[i,j]], axis=0)
                index += 1
                print("index=",index)
                print("firstcoordinate=", firstcoordinate)
                findcorner(i,j,a,firstcoordinate,index)
                break

# driver code
tests = [
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 0]
        ]

index = 0
get_rectangle_coordinates(tests, index)