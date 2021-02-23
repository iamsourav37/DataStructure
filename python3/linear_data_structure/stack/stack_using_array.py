import numpy as np

ARRAY_SIZE = 10


class Stack:
    def __init__(self):
        self._stack_array = np.zeros(ARRAY_SIZE, np.int64)
        self._top = -1

    def is_empty(self):
        return self._top == -1

    def is_full(self):
        return self._top == ARRAY_SIZE-1

    def push(self, data):
        if self.is_full():
            print("Stack is overflow")
            return
        else:
            self._top += 1
            self._stack_array[self._top] = data

    def pop(self):
        if self._top == -1:
            return 'Stack is underflow'
        else:
            data = self._stack_array[self._top]
            self._top -= 1
            return data

    def peek(self):
        if self._top == -1:
            return 'Stack is underflow'
        else:
            return self._stack_array[self._top]

    def size(self):
        return self._top+1

    def display(self):
        if self._top == -1:
            print('Stack is underflow')
        else:
            i = self._top
            while i >= 0:
                print(self._stack_array[i])
                i -= 1


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
            print(f"{s.size()} elements in stack.")
        elif choice == 5:
            s.display()
        elif choice == 6:
            break
        else:
            print("invalid choice")


if __name__ == '__main__':
    main()