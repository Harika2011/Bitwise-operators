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

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def swap(self, x, y):
        if x == y:
            return

        node1 = None
        node2 = None
        temp = self.head

        while temp:
            if temp.data == x:
                node1 = temp
            elif temp.data == y:
                node2 = temp
            temp = temp.next

        if node1 is None or node2 is None:
            print("One or both elements not found")
            return

        node1.data, node2.data = node2.data, node1.data


dll = DoublyLinkedList()

dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.insert(40)

print("Original List:")
dll.display()

a = int(input("Enter first element to swap: "))
b = int(input("Enter second element to swap: "))

dll.swap(a, b)

print("List after swapping:")
dll.display()