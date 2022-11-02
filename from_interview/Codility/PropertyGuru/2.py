def solution(a,b):
    astr= str(a)
    bstr =str(b)
    alen = len(str(a))
    blen=len(str(b))
    result = ""
    o=0
    if alen <= blen:
        alen = blen
    else:
        blen=alen
    for i in range(0,alen+1):
        result += str(astr[i:i+1])
        for j in range(o,blen+1):
            result += str(bstr[j:j+1])
            o += 1
            if int(result) > 100000000:
                # print('more than max=',result)
                return -1
            break
    return int(result)

import random
n = 10
miny = -10
maxy = 10
w=[n]
# for p in range(n):
#     w.append(random.randint(miny,maxy))
# print(w)
# print('res=',solution(w))
# test1 = 1000
# test2 = 10000
test1 = 13579
test2 = 246800
print('dat=',test1,'\ndat=',test2)
print('res=', solution(test1,test2))