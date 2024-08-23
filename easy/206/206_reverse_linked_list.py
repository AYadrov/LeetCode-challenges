# Given the head of a singly linked list, 
# reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        while head:
            next_node = head
            head = head.next
            next_node.next = prev_node
            prev_node = next_node
        return prev_node