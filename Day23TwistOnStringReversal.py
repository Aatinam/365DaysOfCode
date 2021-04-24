#Day 23 of 365 days of code
#Link for leetcode:https://leetcode.com/problems/reverse-only-letters/

#Problem Statement : Given a string S, return the "reversed" string where all characters that are not a 
#letter stay in the same place, and all letters reverse their positions.

class Solution:
    def reverseOnlyLetters(self, S):
        i = 0 ;
        j = len(S) - 1;
        arr = list(S) ##Need to convert to array because string is immutable in python. Note syntax
        while i < j:
            canSwap = True
            if not S[i].isalpha(): ##Cool built in function to see if something is a letter instead of trying to recall ASCII nums
                i+=1
                canSwap = False
                
            if not S[j].isalpha():    
                j-=1
                canSwap = False
            if canSwap:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i+=1
                j-=1
        reversed = ""   
        return reversed.join(arr); ##Convert array back to str
    
   
                