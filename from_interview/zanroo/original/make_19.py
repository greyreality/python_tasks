# Given an array of integers ('source'), return an array with exactly same elements, but
# rearranged them so that every '9' comes right after '1' always. You cannot move '1', but other
# elements can be moved. 'source' contains the same number of 1's and 9's and '1' never
# appears right next to ‘1’.
# make_19(source)
# make_19([9, 1, 5, 1, 5, 9]) → [5, 1, 9, 1, 9, 5]
# make_19([4, 1, 4, 9]) → [4, 1, 9, 4]
# make_19([7, 1, 4, 9, 9, 1, 3]) → [7, 1, 9, 4, 3, 1, 9]
import copy

def make_19(source):
    temp = []
    new_source = copy.deepcopy(source)
    for i in range(0, len(source)):
        if source[i] != 1 :
            if source[i] != 9:
                temp.append(source[i])
            new_source[i] = ''
    for i in range(0, len(new_source)):
        if new_source[i] == 1:
            new_source[i + 1] = 9
    # print('temp=', temp)
    # print('source=', source)
    # print('copy_source=', copy_source)
    for i in range(0, len(new_source)):
        if new_source[i] == '':
            new_source[i] = temp.pop(0)
    return new_source

print(make_19([9, 1, 5, 1, 5, 9]))  # → [5, 1, 9, 1, 9, 5]
print(make_19([4, 1, 4, 9])) #→ [4, 1, 9, 4]
print(make_19([7, 1, 4, 9, 9, 1, 3]))  # → [7, 1, 9, 4, 3, 1, 9]
