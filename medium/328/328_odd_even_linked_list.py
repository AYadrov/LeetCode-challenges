# Given the head of a singly linked list, 
# group all the nodes with odd indices together 
# followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        even_tail_pointer = None
        even_start_pointer = None
        odd_tail_pointer = None
        odd_start_pointer = None

        flag = False
        while curr_node != None:
            if flag:
                # even
                if even_tail_pointer:
                    even_tail_pointer.next = curr_node
                    even_tail_pointer = even_tail_pointer.next
                else:
                    even_tail_pointer = curr_node
                    even_start_pointer = curr_node
                flag=False
            else:
                # odd
                if odd_tail_pointer:
                    odd_tail_pointer.next = curr_node
                    odd_tail_pointer = odd_tail_pointer.next
                else:
                    odd_tail_pointer = curr_node
                    odd_start_pointer = curr_node
                flag=True
            curr_node = curr_node.next
        if even_tail_pointer:
            odd_tail_pointer.next = even_start_pointer
            even_tail_pointer.next = None
        return odd_start_pointer