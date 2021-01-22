class Node:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


def print_linked_list(head):
    s = []
    while head:
        s.append(str(head.val))
        head = head.next
    print(" --> ".join(s))


def create_linked_list(length, function) -> Node:
    head = node = Node(function(1))
    for i in range(2, length + 1):
        node.next = Node(function(i))
        node = node.next
    return head



