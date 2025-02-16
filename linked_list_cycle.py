class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    l = head
    r = head
    while r and r.next:
        l = l.next
        r = r.next.next
        if l == r:
            return True
    return False
    
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next

print(hasCycle(head))