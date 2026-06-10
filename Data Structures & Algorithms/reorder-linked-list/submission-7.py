# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # edge case
        if not head or not head.next:
            return

        # get the second half
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        mid = slow
        prev.next = None

        # print(mid)

        # reorder the second half
        prev = None
        curr = mid
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        newHead = prev

        # print(newHead)

        # merge list
        mergeFirst = True
        dummy = ListNode()
        prev = dummy
        while head and newHead:
            if mergeFirst:
                prev.next = head
                head = head.next
            else:
                prev.next = newHead
                newHead = newHead.next
            prev = prev.next
            mergeFirst = not mergeFirst
        
        if head:
            prev.next = head
        if newHead:
            prev.next = newHead

        return    