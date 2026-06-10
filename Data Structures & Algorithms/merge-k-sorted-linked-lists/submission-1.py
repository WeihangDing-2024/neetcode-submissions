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
            i, j = 0, curr_len - 1
            while i < j:
                lists[i] = self.merge2Lists(lists[i], lists[j])
                i += 1
                j -= 1
            curr_len = j + 1
        
        return lists[0]
    
    def merge2Lists(self, lst1, lst2):
        if not lst1:
            return lst2
        if not lst2:
            return lst1
        
        dummy = ListNode()
        prev = dummy
        while lst1 and lst2:
            if lst1.val < lst2.val:
                prev.next = lst1
                lst1 = lst1.next
            else:
                prev.next = lst2
                lst2 = lst2.next
            prev = prev.next
        
        if lst1:
            prev.next = lst1
        if lst2:
            prev.next = lst2
        return dummy.next
            
        
        