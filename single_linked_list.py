from math import ceil


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    # appends given data at the end of the linkedList
    def append(self, data):
        new_node = Node(data=data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    # returns length of the given nodes
    def __len__(self):
        current_node = self.head
        count = 0
        while current_node.next is not None:
            current_node = current_node.next
            count += 1
        return count

    # returns value of the given elements
    def get(self, index):
        if len(self) < 0 or index >= len(self):
            raise IndexError("Index out of Range")
        current_node = self.head
        current_index = 0
        while current_node.next is not None:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    # helps in getting item using bracket syntax ie a[1]
    def __getitem__(self, item):
        return self.get(index=item)

    # deletes the value with the given index
    def delete_value_with_index(self, index):
        current_node = self.head
        current_index = 0
        while current_node.next is not None:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
            current_index += 1

    # deletes the value with the given value
    def delete_value(self, value):
        current_node = self.head
        current_index = 0
        while current_node.next is not None:
            last_node = current_node
            current_node = current_node.next
            if current_node.data == value:
                last_node.next = current_node.next
            current_index += 1

    # finds the given middle value
    def find_middle_value(self):
        len_of_nodes = len(self)
        middle_index = ceil(len_of_nodes // 2) if len_of_nodes % 2 != 0 else len_of_nodes // 2
        current_node = self.head
        current_index = 0
        while current_node.next is not None:
            current_node = current_node.next
            if current_index == middle_index:
                return current_node.data
            current_index += 1

    # inserts the node at the given index
    def insert(self, index, data):
        if index >= len(self) or len(self) <= 0:
            return self.append(data)
        current_node = self.head
        current_index = 0
        while current_node.next is not None:
            previous_node = current_node.next
            if index == current_index:
                current_node.next = Node(data)
                current_node.next.next = previous_node
                return
            current_node = current_node.next
            current_index += 1

    def insert_node(self, index, data):
        current_index = 0
        current_node = self.head
        while current_node.next is not None:
            previous_node = current_node.next
            if index == current_index:
                current_node.next = Node(data)
                current_node.next.next = previous_node
                return
            current_node = current_node.next
            current_index += 1

    def update_data(self, index, data):
        current_index = 0
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            if current_index == index:
                current_node.data = data
            current_index += 1

    def display(self):
        element_list = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            element_list.append(current_node.data)
        return element_list

    # sort given linked list
    def sort(self):
        current_node = self.head.next
        if self.head is None:
            return
        else:
            while current_node is not None:
                index = current_node.next
                while index is not None:
                    if current_node.data > index.data:
                        current_node.data, index.data = index.data, current_node.data
                    index = index.next
                current_node = current_node.next

    def remove_duplicates(self):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.data == current_node.next.data:
                temp_node = current_node.next.next
                current_node.next = None
                current_node.next = temp_node
            else:
                current_node = current_node.next


if __name__ == '__main__':
    def list_of_obj(linked):
        stupid = []
        for i in linked:
            if i is not None:
                stupid.append(i)
        return stupid


    link = LinkedList()
    link.append(5)
    link.append(5)
    link.append(3)
    link.append(4)
    link.append(5)
    link.append(3)
    # print(len(link))
    # print(link.get(5))
    # print(list_of_obj(link))
    # link.delete_value_with_index(1)
    link.insert(0, 6)
    link.sort()
    link.remove_duplicates()
    print(link.display())
    # print(list_of_obj(link))
    # print(link.find_middle_value())

    # link.insert(2, 99)
    # print(link.display())
