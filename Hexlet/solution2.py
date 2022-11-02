# Создайте функцию find, которая находит элемент в двоичном дереве поиска Binary Search Tree. Дерево представлено в виде массива.
# Ваша функция должна возвращать индекс найденного элемента.
# В случае если дерево (массив) пустое или искомый элемент внутри этого дерева не представлен, функция должна вернуть None.
import math
def find(tree, value):
    # print('tr', tree)

    if tree == []:
        return None

    n = len(tree)
    hight = round(math.log(n, 2))
    # print('hight',hight)
    doit = True
    i = 0
    while doit:
        # print('i=', i, 'value', value)
        if i > n:
            return None
        if value == tree[i]:
            return i
        else:
            if value > tree[i] and i <= 2 * i + 2:
                new = 2 * i + 2
                i = new
            else:
                if value < tree[i] and i <= 2 * i + 1:
                    new = 2 * i + 1
                    i = new
                else:
                    return None
