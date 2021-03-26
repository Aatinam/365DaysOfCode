#Day 11 of 365 days of code
#Link for leetcode: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/

#Problem Statement : Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
# (similar to C/C++'s atoi function).

class Solution:
   def myAtoi(self, s):
        if len(s) == 0:
            return 0;
        i=0
        while(i < len(s) and s[i] == " "):
            i+=1
        if i == len(s):
            return 0;
        isNegative = False;
        if s[i] == "+" or s[i] == "-":
            isNegative = s[i] == "-";
            i+=1;
        if i == len(s):
            return 0;
        
        INT_MAX = (2**31) - 1;
        INT_MIN = -2**31;
        result = 0        
        while(i <len(s) and ord(s[i]) >= ord("0") and ord(s[i]) <= ord("9")): 
            numToAdd = ord(s[i]) - ord("0"); #example: Ascii value of 1 is 49, ascii of 0 is 48. 49-48 = 1
            if result > INT_MAX/10 or (result == INT_MAX/10 and numToAdd > INT_MAX%10):
                if isNegative:
                    return INT_MIN;

                return INT_MAX;
            else:
                result = 10*result + numToAdd;
            i+=1
            
        if isNegative:
            return -1*result;
        return result;

if __name__ == "__main__":
  sol = Solution();
  print(sol.myAtoi("2147483648"));
