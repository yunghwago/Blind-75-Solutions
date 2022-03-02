# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #what is "inverting a tree"?
        #swap left and right of all nodes but the root
        #what do we need to do
        #copy left node to temp
        #assign left node to right
        #assign right node to left

        if root: #python specific way to say if not NULL
            root.left, root.right = root.right, root.left #python specific way to do swaps
            self.invertTree(root.left)
            self.invertTree(root.right)  
        return root  
