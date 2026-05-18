# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if either list is None (or both is None)
        if not list1: return list2
        if not list2: return list1

        # normal case
        curr1 = list1
        curr2 = list2

        # both lists are not None
        fake = ListNode()
        prev = fake
        while curr1 and curr2:
            if curr1.val < curr2.val:
                prev.next = curr1
                prev = prev.next
                curr1 = curr1.next
            else:
                prev.next = curr2
                prev = prev.next
                curr2 = curr2.next
            
        if curr1:
            prev.next = curr1
        
        if curr2:
            prev.next = curr2
        
        return fake.next