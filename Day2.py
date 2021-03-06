
#Day 2 of 365 Days of Code
#Problem Source: https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/625/

#Problem Statement: Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#A valid BST is defined as follows:
### 1. The left subtree of a node contains only nodes with keys less than the node's key.
### 2. The right subtree of a node contains only nodes with keys greater than the node's key.
### 3. Both the left and right subtrees must also be binary search trees.

#It took 2 minutes to write the solution and another 20 minutes to solve all the syntax errors. I have completely 
#forgotten python. The reason this question is easy is because of the definition of BST they use, the left subtree of
#a node contains keys that are strictly less than the node, and the right subtree contains keys strictly greater.
#What would make this interesting would be if left subtree could contain values less than equal to node. Then 
#this solution would no longer work, in particular in the case of duplicate values.  


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBST(self, root):
        def inOrderTraversal( root, arr):
            if (root != None):
                inOrderTraversal(root.left, arr);
                arr.append(root.val);
                inOrderTraversal(root.right, arr);
                return arr;
        
        arr = inOrderTraversal(root, []);
        for i in range(0, len(arr)-1):
            if(arr[i] >= arr[i+1]):
                return False;
        return True;

