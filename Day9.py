

#Day 9 of 365 days of code
#Link for leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

#Problem Statement : Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s):
        #seems like a candidate for sliding window, because we need concurrent elements, and we are looking 
        #for max + can iterate over string. 
        
        maxSubstringLen = 0;
        strLength = len(s);
        if (strLength <= 1):
            return strLength;
        start = 0;
        end = 1;
        charsVisited = [False]*128;
        charsVisited[ord(s[start])] = True;
        while (end < strLength):
            if (not charsVisited[ord(s[end])]):
                charsVisited[ord(s[end])] = True;                
                
            else:
                while (s[start] != s[end]):
                    charsVisited[ord(s[start])] = False;
                    start+=1;
                start+=1
            
            maxSubstringLen = max(maxSubstringLen, end -start+1);
            
            end+=1;
        return maxSubstringLen;