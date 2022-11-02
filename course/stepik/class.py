class MoneyBox:
    def __init__(self, capacity):
        self.balance = 0
        self.capacity = capacity

    def can_add(self, v):
        if self.capacity - self.balance >= v:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.balance += v


x = MoneyBox(5)
