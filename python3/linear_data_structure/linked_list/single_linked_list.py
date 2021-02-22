class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        # self.head = Node(data, self.head)
        node = Node(data, self.head)
        self.head = node
        self.length += 1

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
        else:
            tmp = self.head

            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = Node(data, None)
        self.length += 1

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, data, index):
        if index < 0 or index > self.length:
            raise Exception("Invalid index")
        elif index == 0:
            self.insert_at_beginning(data)
            return
        elif index == self.length:
            self.insert_at_end(data)
        else:
            self.length += 1
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                    return

                itr = itr.next
                count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next
        else:
            print(f"{data_after} is not present in the list")

    def remove_first(self):
        if self.head is None:
            return
        else:
            self.length -= 1
            self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            return
        else:
            self.length -= 1
            itr = self.head
            while itr.next.next:
                itr = itr.next
            itr.next = None

    def remove_at(self, index):
        if index < 0 or index > self.length:
            raise Exception("Invalid index")
        elif index == 0:
            self.remove_first()
            return
        else:
            self.length -= 1
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    return
                itr = itr.next
                count += 1

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
            data_list += 'XXX'
            print(data_list)

    def get_length(self):
        return self.length




def main():
    list = LinkedList()
    list.insert_values(('Sourav', 'Ratul', 'Ashim'))
    list.insert_at('Anish', 3)
    list.insert_at('Nayan', 4)
    list.insert_at('Pritam', 4)
    list.insert_at('Bapi', 3)

    list.insert_after_value('Anish', 'Amartya')
    list.insert_after_value('Sourav', 'Gourab')

    list.display_list()
    print("Length : ", list.get_length())





if __name__ == '__main__':
    main()
