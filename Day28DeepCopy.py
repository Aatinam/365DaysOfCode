#Day 28 of 365 days of code
#Link for leetcode:https://leetcode.com/problems/copy-list-with-random-pointer/

#Problem Statement :  linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
#Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and 
#random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list 
#should point to nodes in the original list.

class Node:
    def __init__(self, x, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        nodeMap = {}
        
        def recursiveCopy(node):
            if node == None:
                return None
            nodeCopy = Node(node.val)
            nodeMap[node] = nodeCopy
            nodeCopy.next = recursiveCopy(node.next)         
            if node.random == None:
                nodeCopy.random = None
            else:
                reqNode = node.random 
                nodeCopy.random = nodeMap[reqNode]
            return nodeCopy

        
        
        newHead = recursiveCopy(head)
        return newHead
      
        
