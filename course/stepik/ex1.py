class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
b = A()

a.bar()
a.foo()

c = A()
print('A class=',A.val)
print('a=',a.val)
print('b=',b.val)
print('c=',c.val)