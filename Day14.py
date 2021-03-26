#Day 14 of 365 days of code
#Link for leetcode:https://leetcode.com/problems/integer-to-roman/

#Problem Statement : Given an integer, convert it to a roman numeral.

class Solution:
    
    def intToRoman_Solution1(self, num):
        numToRomanDict = {
          1: "I",
          4: "IV",
          5: "V",
          9: "IX",
          10: "X",
          40: "XL",
          50: "L",
          90: "XC",
          100: "C",
          400: "CD"  ,
          500: "D",
          900: "CM",
          1000: "M"
        };
        romanDictKeys = list(numToRomanDict.keys());
        romanEquiv = "";
        
        while(num!= 0):
            start = 0;
            end = len(romanDictKeys);             
            while (start != end):
                mid = start + ((end-start)//2);
                if (romanDictKeys[mid] > num):
                    end = mid;
                else: #  romanDictKeys[mid] <= num
                    if mid+1 >= len(romanDictKeys) or num < romanDictKeys[mid + 1]:
                        num = num - romanDictKeys[mid];
                        romanEquiv += numToRomanDict[romanDictKeys[mid]];
                        break;
                    else:
                        start = mid;
                        
        return romanEquiv;

    def intToRoman_Solution2(self, num):
        ####Note Dictionary is in opposite direction i.e at index 0 we have 1000
        ##O(1) runtime
          numToRomanDict = {
          1000: "M",
          900: "CM",
          500: "D",
          400: "CD",
          100: "C",
          90: "XC",
          50: "L",
          40: "XL",
          10: "X",
          9: "IX",
          5: "V",
          4: "IV",
          1: "I"
        };
          
          intKeys = list(numToRomanDict.keys());
          romanEquiv = "";
          i=0
          while(i < len(intKeys)):
              romanEquiv += num//intKeys[i] * numToRomanDict[intKeys[i]];
              num = num % intKeys[i];
              i+=1           
          return romanEquiv;
    