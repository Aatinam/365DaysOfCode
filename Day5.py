#Day 5 of 365 Days of Code
#Problem Source: https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/

#Problem Statement: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
#and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2) :
        
        def helper (l1, l2, k):
            if l1 == None and l2 == None and k == 0:
                return None;
            sum = k;
            next1 = None;
            next2 = None;
            if l1 != None:
                sum += l1.val;
                next1 = l1.next;
            if l2 != None:
                sum += l2.val;
                next2 = l2.next;
            n = ListNode(sum%10);
            new_k = 0
            if (sum >= 10):
                new_k = 1 
            n.next = helper(next1, next2, new_k);
            return n;
        return helper(l1, l2, 0);
            