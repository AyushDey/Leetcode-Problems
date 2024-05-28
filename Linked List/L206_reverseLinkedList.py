# Input : 1 -> 2 -> 3 -> Null
# Output : 3 -> 2 -> 1 -> Null

class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

def createList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def reverseList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def printList(head):
    current = head
    while current:
        if current.next is None:
            print(current.val)
        else:
            print(current.val, end=' -> ')
        current = current.next

if __name__ == '__main__':
    values = list(map(int, input().strip().split()))
    linked_list = createList(values)
    print("Original List:")
    printList(linked_list)
    reverse_list = reverseList(linked_list)
    print("Reversed List:")
    printList(reverse_list)
