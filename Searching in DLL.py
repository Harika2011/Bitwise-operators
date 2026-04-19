class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def search(self, key):
        temp = self.head
        pos = 1

        while temp is not None:
            if temp.data == key:
                print("Element found at position", pos)
                return
            temp = temp.next
            pos += 1

        print("Element not found")


dll = DoublyLinkedList()

dll.insert(5)
dll.insert(10)
dll.insert(15)
dll.insert(20)

num = int(input("Enter element to search: "))
dll.search(num)