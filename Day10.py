

#Day 10 of 365 days of code
#Link for leetcode: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/

#Problem Statement : Given a string s, return the longest palindromic substring in s.



class Solution:
    def longestPalindrome( s) :
        strLen = len(s);
        start = 0
        end = 0;
      ##  isPalindrome= [[False]*strLen]*strLen; This is how I was initially creating list.  When you write [x]*3 you get, essentially, 
      ## the list [x, x, x]. That is, a list with 3 references to the same x. When you then modify this single x it is visible via all three references to it  
      ## to fix this you need to do the following, don't forget!!!:
        isPalindrome = [[False for y in range(strLen)] for x in range(strLen)];

        for i in range (strLen-1,-1,-1):
            for j in range(i, strLen):
                if s[i] == s[j]:
                    if i == j or i+1 == j:
                        isPalindrome[i][j] = True;
                    else:                       
                        isPalindrome[i][j] = isPalindrome[i+1][j-1]
                if isPalindrome[i][j] and j-i> end-start:
                    start = i;
                    end = j;
        return s[start:end+1];

    if __name__ == "__main__":
        print(longestPalindrome("babad"));
