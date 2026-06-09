# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # 1. find the head of the second half of the linked list
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        head_2nd = slow
        prev.next = None

        # 2. reverse the order of the second half
        curr_node = head_2nd
        prev_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        reversed_head = prev_node

        # 3. merge them one by one 
        append_first = True
        curr_1st = head
        curr_2nd = reversed_head
        fake = ListNode()
        prev = fake
        while curr_1st and curr_2nd:
            if append_first:
                prev.next = curr_1st
                curr_1st = curr_1st.next
            else:
                prev.next = curr_2nd
                curr_2nd = curr_2nd.next
            prev = prev.next
            append_first = not append_first
        prev.next = curr_2nd
