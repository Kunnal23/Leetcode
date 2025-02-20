# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head,val):
    if not head:
        return None
    temp = ListNode(0, head)
    curr = temp
    while curr.next != None:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return temp.next

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)


# Helper function for print the list
def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

printList(removeElements(head,1))
# printList(head)
