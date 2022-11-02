# Given an array of integers ('source'), return an array with exactly same elements, but
# rearranged them so that every '9' comes right after '1' always. You cannot move '1', but other
# elements can be moved. 'source' contains the same number of 1's and 9's and '1' never
# appears right next to ‘1’.
# make_19(source)
# make_19([9, 1, 5, 1, 5, 9]) → [5, 1, 9, 1, 9, 5]
# make_19([4, 1, 4, 9]) → [4, 1, 9, 4]
# make_19([7, 1, 4, 9, 9, 1, 3]) → [7, 1, 9, 4, 3, 1, 9]

def make_19(source):
    i, j = 0, 0

    while (1 in source[i:]):
        print('source',source[i:])
        # str.index(str, beg=0, end = len(string)) return Index if found otherwise raises an exception if str is not found.
        print('index for 1, i=',source.index(1, i) + 1)
        i = source.index(1, i) + 1
        print('index for 9, j=', source.index(9, j) + 1)
        j = source.index(9, j) + 1
        print('source[i]=', source[i])
        print('source[j-1]', source[j-1])
        source[j - 1] = source[i]
        source[i] = 9
        print('i==', i+1)
        print('j==', j)
        j = max(i + 1, j)
        print('max j==', j)

    return source


# print(make_19([9, 1, 5, 1, 5, 9]))  # → [5, 1, 9, 1, 9, 5]
# print(make_19([4, 1, 4, 9]))  # → [4, 1, 9, 4]
print(make_19([7, 1, 4, 9, 9, 1, 3]))  # → [7, 1, 9, 4, 3, 1, 9]
