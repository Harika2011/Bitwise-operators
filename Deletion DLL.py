class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

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

def delete_value(head, key):
    temp = head

    while temp:
        if temp.data == key:

            if temp.prev is None:
                head = temp.next
                if head:
                    head.prev = None

            elif temp.next is None:
                temp.prev.next = None

            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev

            return head

        temp = temp.next

    print("Value not found")
    return head

def delete_beginning(head):
    if head is None or head.next is None:
        return None

    head = head.next
    head.prev = None
    return head

def delete_end(head):
    if head is None or head.next is None:
        return None

    temp = head
    while temp.next:
        temp = temp.next

    temp.prev.next = None
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
    head = insert_end(head, value)

print("Original List:")
print_list(head)

key = int(input("Enter value to delete: "))
head = delete_value(head, key)

print("After deleting value:")
print_list(head)

head = delete_beginning(head)
print("After deleting from beginning:")
print_list(head)

head = delete_end(head)
print("After deleting from end:")
print_list(head)
 