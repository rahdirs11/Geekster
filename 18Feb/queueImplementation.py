class EmptyQueueException(IndexError):
    def __init__(self, msg):
        super().__init__('EmptyQueueException <{}>'.format(msg))


class FullQueueException(IndexError):
    def __init__(self, msg):
        super().__init__("FullQueueException <{}>".format(msg))


class Queue:
    def __init__(self):
        self.MAXSIZE = 5
        self.array = []
        self.front, self.rear = -1, -1

    def enqueue(self, val):
        if not self.isFull():
            self.front += 1
            self.array.append(val)
        else:
            raise FullQueueException('THE QUEUE IS FULL, CAN\'T INSERT NEW ELEMENTS')
    
    def dequeue(self):
        if not self.isEmpty():
            val = self.array[0]
            self.array.pop(0)
            self.rear += 1
            return val
        else:
            raise EmptyQueueException('NO ELEMENTS LEFT IN QUEUE TO BE REMOVED')
            # print('Empty queue')
    
    def isEmpty(self):
        return self.front == -1 or self.rear > self.front - 1
    
    def isFull(self):
        return self.front == self.MAXSIZE - 1
    
    def display(self):
        if len(self.array) == 0:
            print('Empty Queue')
            return
        for i in self.array:
            print(i, end=" ")
        print()


q = Queue()
try:
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.display()
    # q.enqueue(60)

    q.dequeue()
    q.dequeue()

    q.display()

    q.dequeue()
    q.dequeue()

    q.display()
    q.dequeue()

    q.dequeue()
except EmptyQueueException as e:
    print(e)
except FullQueueException as e:
    print(e)