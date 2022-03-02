# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        solution: convert bst to list, removing null values
        return k-1th (we have to account for the 0th index in an array) entry of that list
        """
        
        values = []
        def dfsHelper(root, values):
            if not root:
                return
            else:
                values.append(root.val)
                dfsHelper(root.left, values)
                dfsHelper(root.right, values)
        dfsHelper(root, values)
        values.sort()
        return values[k-1]
