class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return -1

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return -1

    def size(self):
        return len(self.items)

    def display(self):
        if self.items:
            for val in self.items[::-1]:
                print(val)
        else:
            print("stack is empty")


def main():
    s = Stack()
    while True:
        print('1. push')
        print('2. pop')
        print('3. peek')
        print('4. size')
        print('5. display')
        print('6. quit')

        choice = int(input('enter your choice : '))

        if choice == 1:
            data = int(input('enter data : '))
            s.push(data)
        elif choice == 2:
            print(s.pop())
        elif choice == 3:
            print(s.peek())
        elif choice == 4:
            print("Size of stack is : ", s.size())
        elif choice == 5:
            s.display()
        elif choice == 6:
            break
        else:
            print("invalid choice")



if __name__ == '__main__':
    main()
