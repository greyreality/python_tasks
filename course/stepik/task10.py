def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                print('pp=',newpath)
                return newpath
    return None


def g(c):
    d = {}
    size = int(c[0])
    for item in range(1, size + 1):
        if ' : ' in c[item]:
            class1, class2 = c[item].split(' : ')
            # print('class1=', class1, 'class2=', class2)
            classes2 = class2.split(' ')
            for k in classes2:
                if k in d.keys():
                    d[k].append(class1)
                else:
                    d[str(k)] = []
                    d[k].append(class1)
    # for j in d:
    #     print('key=', j, 'value=', d[j])
    # print(d)
    return d

n = int(input())
# print('num=',n)
inp = []
inp.append(n)

for i in range (1,n+1):
    inp.append(input())
# print(inp)

n = int(input())
# print('num2=',n)
inp2 = []
inp2.append(n)

for i in range (1,n+1):
    inp2.append(input())
# print(inp2)


# with open("input.txt", "r") as f:
#     content = f.readlines()
# content = [x.strip() for x in content]
# print(content)
# graph = g(content)

for i in range (1,inp2[0]+1):
    parent, child = inp2[i].split(' ')
    # print(inp2[i].split(' '))
    if find_path(g(inp), parent, child) != None:
        print('Yes')
    else:
        print('No')


# test data from input.txt
# 12
# G : F
# AA
# B : AA
# C : AA
# D : B C
# E : D
# F : D
# X
# Y : X AA
# Z : X
# V : Z Y
# W : V
# 8
# AA G
# AA Z
# AA W
# X W
# X QWE
# A X
# X X
# 1 1