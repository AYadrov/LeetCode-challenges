# You are given the root of a binary tree.
# A ZigZag path for a binary tree is defined as follow:
# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; 
# otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
# Return the longest ZigZag path contained in that tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # The function simply returns: given a root, low long is zigzag sequence in leaves
        def zigzag(root):
            if root:
                right_r, left_r, side_r = zigzag(root.right) if root.right else (-1, -1, 0)
                right_l, left_l, side_l = zigzag(root.left) if root.left else (-1, -1, 0)
                side = max(right_r, left_l, side_r, side_l)
                return left_r+1, right_l+1, side
            else:
                return -1, -1, 0
        return max(zigzag(root))