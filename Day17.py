#Day 17 of 365 days of code
#Link for leetcode:https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

#Problem Statement : Given a string s, return the maximum number of ocurrences of any substring under the following rules:
##The number of unique characters in the substring must be less than or equal to maxLetters.
#The substring size must be between minSize and maxSize inclusive.


class Solution:
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        if len(s) < minSize:
            return 0
        
        start = 0      
        subStringCount = {}
        
        for end in range(minSize, len(s)+1):
            subStr = s[start:end]
            if subStr in subStringCount:
                subStringCount[subStr] +=1;
            else:
                subStringCount[subStr] = 1;
                
            if (end-start) >= minSize:
                start+=1
        maxFreq = 0
        for subStrs in subStringCount:
            chars = set()
            numUniqueChars = 0
            for char in subStrs:
                if char not in chars:
                    numUniqueChars +=1;
                    chars.add(char);
            if numUniqueChars <= maxLetters:
                maxFreq = max(maxFreq, subStringCount[subStrs])
        
        return maxFreq;
                


if __name__ == "__main__":
    s = Solution();
    s.maxFreq("abcde", 2,3,3)
                