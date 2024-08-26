# Given the root of a binary tree, 
# imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def right_search(root):
            if root:
                right = right_search(root.right)
                left = right_search(root.left)
                if len(right) >= len(left):
                    return [root.val] + right
                else:
                    return [root.val] + right + left[len(right):]
            else:
                return []
        return right_search(root)