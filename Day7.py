
#Day 7 of 365 days of code
#ILink for leetcode: https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/

#Problem Statement :Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
#(i.e., from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        ans = [];
        queue = [];
        if (root == None):
            return ans;
        
        queue.append(root);            
        rightFirst = True;
        
        while(len(queue) != 0):            
            size = len(queue);
            level = [];            
            while size > 0:
                n = queue.pop(0);
                size -=1;
                if rightFirst:
                    level.append(n.val);
                else:
                    level.insert(0,n.val);
                if(n.left != None):
                    queue.append(n.left);
                if(n.right != None):
                    queue.append(n.right);
                
            if(len(level) > 0):            
                ans.append(level);
            rightFirst = not rightFirst;
            
        return ans;
                     