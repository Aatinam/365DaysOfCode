#Day 11 of 365 days of code
#Link for leetcode: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/

#Problem Statement : Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
# (similar to C/C++'s atoi function).

class Solution:
    def indexOfFirstNonWhitSpaceChar(self, s):
        i = 0;
        while(i<len(s) and s[i] == " "):
            i+=1;
        return min(i, len(s)-1);
    
    def getIndexOfFirstNumIfAny(self, s, i):
        if s[i] == "-" or s[i]== "+":
            i= i+1;
        while(i < len(s) and s[i] == "0"):
            i+=1;
        if i>= len(s) or s[i] not in "123456789":
            return -1;
        else:
            return i;
        
    def getIndexOfLastNum(self, s, i):
        j=i;
        while(j < len(s) and s[j] in "0123456789"):
            j+=1;
        return j;

    def clampNumIfRequired(self, num):
        lowerBound = -2**31;
        upperBound = 2**31 - 1;
        if num < lowerBound:
            return lowerBound;
        if num > upperBound:
            return upperBound;
        return num;
    
    def myAtoi(self, s):
        if len(s) < 1:
            return 0;
        i = self.indexOfFirstNonWhitSpaceChar(s);        
        isNegative = s[i] == "-";
        i = self.getIndexOfFirstNumIfAny(s, i);
        if i == -1:
            return 0;
        j = self.getIndexOfLastNum(s, i);
        requiredSubstring = s[i:j];
        requiredNum = int(requiredSubstring); 
        if isNegative:
            requiredNum = requiredNum*-1;
        finalNum = self.clampNumIfRequired(requiredNum);
        return finalNum;
        

if __name__ == "__main__":
  sol = Solution();
  print(sol.myAtoi("+-12"));
