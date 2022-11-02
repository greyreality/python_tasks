# def sort(a):
#     prev = -1
#     sorted = []
#     l = len(a)
#
#     for i in a:
#         if i < prev:
#             sorted.append(i)
#             print(sorted)
#         else:
#             a[a.index(i)] = prev
#         prev = i
#     return sorted

def sort(str1):
    leng = len(str1)
    result = []
    for i in str1:
        if i not in result:
            result.append(i)
        # print(i)
    makeitastring = ''.join(map(str, result))
    return makeitastring

a = [1,5,3,4,5,0]
b =1
c =2
str1 = "hello"
print(sort(str1))