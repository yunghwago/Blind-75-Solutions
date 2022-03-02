# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        """
        what do we know given preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]?
        3 is the root, 9 is root.left, 20 is root.right
        so the first 3 values of any given preorder traversal are the root, left, and right respectively

        now if we remove those numbers from our inorder list, we get [15,7]
        15 and 7 are the numbers that surround 20, and we know that inorder traversal goes L->R, so we know that 15 and 7 are attached to 20 (and not 9)
        and that 15 is to the left of 20, and 7 is to the right of 20

        an easy way to handle this, is to place a pointer at 3 in the inorder traversal list, and say that everything to the left of our 3 is on the left
        side of the tree, and everything to the right of the 3 is on the right side of the tree
        we can use this information to help us, because we can calculate the sizes of the left and right sides of the tree using our root of tree pointer
        to the left of 3 there is 1 number, and to the right of 3 there are 3 numbers, so we know that the left subtree will have a size of 1 node, and the
        right subtree will have a size of 3 nodes

        how do we choose the root of our subtree?
        we can just take the middle of the half. we know that 20 is the root of its subtree because it is in the middle of the right half of the array, and we
        can recursively obtain the middle after left and right halves are determined

        more questions:
        given this information what is our algo?
        what data structures would we use to a. construct our tree and b. maintain the nodes that have already been inserted into the tree, on both preorder
        and inorder lists? so that we don't insert duplicate nodes?

        """   
        #handle base cases
        if not preorder or not inorder:
            return None        
    
        #initialize root and mid given what we know
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) #index is a python specific function
    
        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid]) #pass in the new preorder and inorder arrays as sublists, which is also a python specific thing
        #note: sublists' 2nd bound is non-inclusive, so we're actually passing in the elements in preorder all the way to mid
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:]) #sublists in this node are every element after the elements passed in left for both trees
    
    
        return root
