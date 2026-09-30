#type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return root
        else:
            current = root
            new_right = current.left
            new_left = current.right
            current.right = self.invertTree(new_right)
            current.left = self.invertTree(new_left)
            return root