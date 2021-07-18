#Day 30 of 365 days of code
#Link for leetcode: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
#Problem Statement : Given two strings s and part, perform the following operation on s until all occurrences of the substring part 
#are removed:
    #Find the leftmost occurrence of the substring part and remove it from s.
#Return s after removing all occurrences of part.
   
    
class Solution:    
    def removeOccurrences(self, s, part):
            stack= []
            for char in s:
                stack.append(char)
                if len(stack) >= len(part) and "".join(stack[-len(part):]) == part:
                    count = len(part)
                    while (count > 0):
                        stack.pop()
                        count-=1
                        
            return "".join(stack)

