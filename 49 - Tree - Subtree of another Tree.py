# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self, root, subRoot):
        #handle base cases
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
                    self.sameTree(root.right, subRoot.right)) #return True if both left and right are the same
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        implementation: compare current node's value to subroot's root
        if they are not equal, iterate through the tree until it is found
        once it is found, run sameTree on it
        """
        #handle base cases 
        if not subRoot: #null is a subtree of every BST
            return True
        if not root:
            return False        
        
        if (self.sameTree(root, subRoot)):
            return True
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
        
        #note for sameTree we need to account for the fact that the original tree might have matching components in the right place to subRoot, but subRoot has
        #more depth with values that are not in the original tree
        """
        ex
        original tree    subtree
           1                1
          /\               /\
         2  3             2  3
                              \
                               4
        """
