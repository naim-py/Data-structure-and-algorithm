class Queue:                # class
    def __init__(self):     # constractor
        self.elements = []  # list implement
    def enqueue(self,data):
        self.elements.append(data)  # data element a append hbe
    def dequeue(self):
        # [1 ,2 ,3 ,4]
        # first valu return krbe pop
        return self.elements.pop(0)

    def rear(self):
        # last valu return krbe rear
        return self.elements[-1]
    def front(self):
        # 0 indedx valu return krbe front
        return self.elements[0]
    def isempty(self):
        return len(self.elements) ==0

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.front())
print("rear : ",q.rear())

q.dequeue()
print(q.front())
print("rear : ",q.rear())

