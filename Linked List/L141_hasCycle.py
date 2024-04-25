# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, 
# where the tail connects to the 1st node (0-indexed).
# 3 -> 2 -> 0 -> 4
#      |         |  
#      -----------
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
start = None
head = [3,2,0,-4]
for i in head:
    newNode = ListNode(i)
    if start is None:
        start = newNode
    else:
        current = start
        while current.next:
            current = current.next
        current.next = newNode


