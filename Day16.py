#Day 16 of 365 days of code
#Link for leetcode:https://leetcode.com/problems/daily-temperatures/

#Problem Statement : Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait 
#until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
#For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

class Solution:
    def dailyTemperatures(self, T):
     
        solSet = [0]*len(T);
        stack = []
        
        for currDay in range(0, len(T)):
            if len(stack) == 0 or T[currDay] <= T[stack[-1]]:
                stack.append(currDay);
            
            else:
                while(len(stack) > 0 and T[currDay] > T[stack[-1]]):
                    prevDay = stack.pop(-1);
                    solSet[prevDay] = currDay - prevDay;
                    
                stack.append(currDay);
                
        
        return solSet;

##### At first glance the time complexity seems to be O(n^2). This is not true, time complexity is O(n).
##### This is because ofr any give T[i], the stack can contain at most elements from 30,....T[i] (See note that temp is in range [30, 100]). 

        