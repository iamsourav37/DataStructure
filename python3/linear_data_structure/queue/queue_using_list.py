# implementation way 0
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()
        else:
            return -1

    def display(self):
        if not self.is_empty():
            for val in self.queue[::-1]:
                print(val)
        else:
            print("queue is empty")


# implementation way 1
class Queue2:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return -1

    def display(self):
        if not self.is_empty():
            for val in self.queue:
                print(val)
        else:
            print("Queue is empty")


def main():
    queue = Queue()

    queue.enqueue(12)
    queue.enqueue(27)
    queue.enqueue(72)
    queue.enqueue(65)
    queue.enqueue(87)

    queue.display()

    queue.dequeue()
    queue.dequeue()

    print("after deleting 2 data")
    queue.display()

    # Queue 2
    print("Queue2 : ")
    queue2 = Queue2()

    queue2.enqueue('Sourav')
    queue2.enqueue('Prosenjit')
    queue2.enqueue('Debangshu')
    queue2.display()

    queue2.dequeue()
    print("after deleting 1 element")
    queue2.display()


if __name__ == '__main__':
    main()
