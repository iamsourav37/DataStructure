import collections
import queue


def main():
    stack = collections.deque()
    stack.append(12)
    stack.append(21)
    stack.append(14)

    print("all the elements in stack: ")
    for val in stack:
        print(val)

    print("Peek element : ", stack[-1])
    stack.pop()
    stack.pop()
    print("now stack is : ", stack)

    # stack using lifo queue

    stack2 = queue.LifoQueue()
    stack2.put('Sourav')
    stack2.put('Ratul')
    stack2.put('Amartya')


if __name__ == '__main__':
    main()