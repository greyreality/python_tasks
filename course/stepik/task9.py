class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.lst = []
        self.max = 5

    def add(self, *a):
        # добавить следующую часть последовательности
        for i in a:
            # print('before', self.lst)
            while len(self.lst) < 5:
                self.lst.append(i)
                # print('added ', i,'into',self.lst)
                break
            if len(self.lst) > 5:
                self.lst.append(i)

            elif len(self.lst) == 5:
                print(sum(self.lst[:5]))
                del self.lst[:5]
                #         print('after', self.lst)
                # print()

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        # print('cur part', self.lst)
        return self.lst


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()  # вернуть [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part()  # вернуть [6]
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part()  # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part()  # вернуть [1]
