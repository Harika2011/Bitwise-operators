class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insert_beginning(head, value):
    new_node = Node(value)
    if head is not None:
        head.prev = new_node
        new_node.next = head
    return new_node

def insert_end(head, value):
    new_node = Node(value)
    if head is None:
        return new_node

    temp = head
    while temp.next:
        temp = temp.next

    temp.next = new_node
    new_node.prev = temp
    return head

def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")

head = None

n = int(input("Enter number of nodes: "))

for _ in range(n):
    value = int(input("Enter value: "))
    choice = int(input("1.Insert at Beginning  2.Insert at End: "))

    if choice == 1:
        head = insert_beginning(head, value)
    elif choice == 2:
        head = insert_end(head, value)

print("Doubly Linked List:")
print_list(head)

