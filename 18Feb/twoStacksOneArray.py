# 0 - 4 for first stack
# 5 - 9 for second
class StackFullException(IndexError):
    def __init__(self, msg):
        super().__init__(msg)


class StackEmptyException(IndexError):
    def __init__(self, msg):
        super().__init__(msg)


class TwoStacks:
    def __init__(self):
        self.MAXSIZE = 10
        self.top1 = self.top2 = -1
        self.array = [0 for _ in range(10)]
    
    @property
    def isFull1(self):
        return self.top == self.MAXSIZE // 2 - 1

    def push1(self, val):
        if not isFull1:
            self.top1 += 1
            self.array[self.top1] = val
        else:
            raise StackFullException('Stack 1 is full - can\'t push new elements!')
    
    @property
    def isFull2(self):
        return self.top2 == self.MAXSIZE - 1

    @property
    def isEmpty1(self):
        return self.top1 == -1

    @property
    def isEmpty2(self):
        return self.top2 == 4

    def push2(self, val):
        if not isFull2:
            self.top2 += 1
            self.array[self.top2] = val
        else:
            raise StackFullException('Stack 2 is full - can\'t push new elements!')
    
    def pop1(self):
        if not isEmpty1:
            val = self.array[self.top1]
            self.top1 -= 1
            return val
        else:
            raise StackEmptyException('Stack 1 is empty - can\'t pop an element!')
    
    def pop2(self):
        if not isEmpty2:
            val = self.array[self.top2]
            self.top2 -= 1
            return val
        else:
            raise StackEmptyException('Stack 2 is empty - can\'t pop an element!')