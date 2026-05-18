# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        curr_len = len(lists)
        while curr_len > 1:
            i = 0
            j = curr_len - 1
            while i < j:
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
                i += 1
                j -= 1
            curr_len = (curr_len - 1) // 2 + 1
        return lists[0]

    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        fake = ListNode()
        prev = fake
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        
        if list1:
            prev.next = list1
        
        if list2:
            prev.next = list2

        return fake.next
        
        