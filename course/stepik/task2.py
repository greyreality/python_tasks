# x = [1,2,3]
# y = x
# print(type(x))
# print(type(y))
# print(type(4))
# print(type(type(4)))

# print(y is x)
# print(y is [1,2,3])

objects = [1, 2, 3, 3, {1}, 1,68]
r = []
ans = 0
n = len(objects)
for i in range(0, n):
    print('i=',i)
    for j in range(i, n):
        print('j=',j)
        if (id(objects[i])) != (id(objects[j])) or j == n -1 :
            if objects[i] not in r:
                r.append(objects[i])
print(len(r))