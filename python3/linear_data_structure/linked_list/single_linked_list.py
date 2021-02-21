class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        # self.head = Node(data, self.head)
        node = Node(data, self.head)
        self.head = node

    def display_list(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            itr = self.head
            data_list = ''
            while itr:
                data_list += str(itr.data) + '-->'
                itr = itr.next
            data_list += 'None'
            print(data_list)


def main():
    list = LinkedList()
    list.insert_at_beginning(12)
    list.insert_at_beginning(72)
    list.insert_at_beginning(34)
    list.insert_at_beginning(10)
    list.insert_at_beginning(8)

    list.display_list()


if __name__ == '__main__':
    main()
