# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. find the length of the linked list
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        # 2. find the Nth node from the end
        # remove the first node
        if n == length:
            return head.next
        
        m = length - n + 1
        prev_node = None
        curr_node = head
        while m > 1:
            prev_node = curr_node
            curr_node = curr_node.next
            m -= 1
        prev_node.next = curr_node.next

        return head