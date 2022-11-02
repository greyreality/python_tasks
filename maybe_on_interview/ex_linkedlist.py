# класс Node для определения элемента списка
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):  # str для распечатки
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' + str(current.value) + '\n'
            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):  # для очистки
        self.__init__()

    def add(self, x):
        self.length += 1
        if self.first == None:
            self.last = self.first = Node(x, None)  # self.first и self.last будут указывать на одну область памяти
        else:
            result = Node(x, None)  # здесь, уже на разные, т.к. произошло присваивание
            self.last.next = result  # firsty присваивается next
            self.last = result
# Если размер связного списка известен, k-й элемент с конца легко вычислить (длина — k).
# Нужно пройтись по списку и найти этот элемент.
def nthtolast(head, k):
    # print('head.value =',head.value)
    if head.next is None:
        return 0
    i = nthtolast(head.next, k) + 1
    # print('i=',i)
    if i == k-1:
        print('№',k,'from the end element is =', head.value)
    return i
# Дано: односвязный список N1->N2->N3->...->Nn и указатель на его голову N1.
# Нужно: развернуть список за один проход так, чтобы стало Nn->Nn-1->Nn-2->...->N1.
def reverse_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail
# def invertList(tail):
#     if tail.value is None:
#         return None
#     else:
#         result = LinkedList()
#         result.add(tail.value)
#         while(tail.value is not None):
#             tail = tail.next
#             result.add(tail.value, result.value)
#         return result
# public static Node invertList(Node tail){
# if (tail==null)return null;
# else {
# Node result = new Node(tail.value, null);
# while (tail.next != null) {
# tail = tail.next;
# result = new Node(tail.value,result);
# }
# return result;
# }
# }
L  = LinkedList()
R = LinkedList()
L.add(1)
L.add(2)
L.add(3)
L.add(4)
L.add(5)
L.add(6)
print('before=',L)
# nthtolast(L.first, 2)
# print('result=',invertList(L.last))
reverse_list(L.first)
print('after=',L)
# В информатике, свя́зный спи́сок — структура данных, состоящая из узлов,
# каждый из которых содержит как собственные данные, так и одну или две ссылки
# («связки») на следующий и/или предыдущий узел списка.
# Принципиальным преимуществом перед массивом является структурная гибкость:
# порядок элементов связного списка может не совпадать с порядком расположения элементов данных в памяти компьютера,
# а порядок обхода списка всегда явно задаётся его внутренними связями.
#  реализация односвязного (однонаправленного) списка
# Недостаток связных списков – это последовательный доступ (sequential access) к элементам,
# тогда как для массивов время доступа постоянно и не зависит от размера - random access.
# Если приложению требуется быстрый поиск элемента по индексу, то в данном случае списки не подходят,
# и лучше воспользоваться массивами.
# Еще один негативный момент при использовании связных списков связан с нерациональным использованием памяти.
# Если в узле хранится небольшая порция данных, например, булевское значение, то список становится неэффективными из-за того,
# что объем памяти, выделяемой под хранение связей, превышает объем памяти, выделяемой под хранение «полезной нагрузки».
# Преимущества:
# 1)Удаление элементов в таком списке более эффективно, нежели удаление элементов из стандартного списка Python,
# 2) То же самое можно сказать и про вставку элементов - она выполняется так же эффективно, как и удаление.
# 3)Объединение или разбиение 2-х списков будет выполняться быстрее, нежели в стандартном варианте.
# 4) элемент такого списка может иметь произвольную структуру, и включать не одну,
# а сразу несколько ссылок, что является отличительной особенностью деревьев.
# Недостатки:
# 1) Требуется выделять дополнительную память на ссылки, которые сами по себе не несут никакой полезной информации.
# 2) Доступ к произвольному элементу для стандартного массива в Си и для стандартного списка в Python
# есть величина постоянная и не зависящая от величины массива. В случае со ссылочными списками время доступа будет зависеть
# от величины списка, так как потребуется выполнить итерацию по всему списку.
