#Day 34 of 365 days of code
#Link for leetcode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#Problem Statement : Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary 
#tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:mid+1] , inorder[0:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root

if __name__ == "__main__":
   s = Solution()
   s.buildTree([3,9,20,15,7],[9,3,15,20,7] )