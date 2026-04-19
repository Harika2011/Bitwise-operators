class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_list():
    n = int(input("Enter number of nodes: "))
    if n == 0:
        return None

    head = Node(int(input("Enter value: ")))
    temp = head

    for _ in range(n - 1):
        value = int(input("Enter value: "))
        temp.next = Node(value)
        temp = temp.next

    return head

def swap_pairs(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first

    return dummy.next

def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" --> ")
        temp = temp.next
    print("None")

head = create_list()

print("Original List:")
print_list(head)

head = swap_pairs(head)

print("After Swapping:")
print_list(head) 
