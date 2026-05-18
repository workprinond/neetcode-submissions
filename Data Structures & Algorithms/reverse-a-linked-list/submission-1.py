# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: [ListNode]) -> Optional[ListNode]:
 
        prev = None
        current = head
        
        while current:
            next_temp = current.next  # Store next node
            current.next = prev       # Reverse the pointer
            prev = current            # Move prev forward
            current = next_temp       # Move current forward
        
        return prev