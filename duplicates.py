class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(values):
    head = None
    tail = None

    for value in values:
        new_node = Node(value)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head


def remove_duplicates(head):
    current = head

    while current and current.next:
        if current.data == current.next.data:
            # Skip the duplicate node
            current.next = current.next.next
        else:
            current = current.next

    return head


def print_linked_list(head):
    values = []
    current = head

    while current:
        values.append(str(current.data))
        current = current.next

    print(" -> ".join(values) if values else "Empty list")


values = list(map(int, input("Enter sorted list elements: ").split()))

head = create_linked_list(values)
head = remove_duplicates(head)

print("List after removing duplicates:")
print_linked_list(head)