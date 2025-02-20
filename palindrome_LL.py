# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#    TIME Complexity: O(n) , SPACE Complexity: O(n)

# def isPalindrome(head):
#     nums = []
#     while head:
#         nums.append(head.val)
#         head=head.next

#     left,right = 0 ,len(nums)-1
#     while left <= right :
#         if nums[left] != nums[right]:
#             return False
#         left+=1
#         right-=1
#     return True

def reverseLL(head):
    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def isPalindrome(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    rev = reverseLL(slow)
    while rev:
        if head.val != rev.val:
            return False
        head = head.next
        rev = rev.next
    return True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)


print(isPalindrome(head))
