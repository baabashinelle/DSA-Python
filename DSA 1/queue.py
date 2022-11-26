# queue implementation in python using lists

class Queue:

    def __init__(self):
        self.queue = []
    
    # add an element
    def enqueue(self, item):
        self.queue.append(item)
    
    # remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # display the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()