
#Day 1 of 365 days of code
#I solved the following question from leetcode: https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/572/

#Problem Statement 
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#The following was my initial solution, I later realized I could make it faster by combining both for loops. 


class Solution:
    def maxProfit(prices):
        length = len(prices);
        M = [0]*length; 
        for i in range(length -2, -1, -1):
            M[i] = max(M[i+1], prices[i+1]);
            
        max_profit = 0;
        for i in range(0, length):
            max_profit = max(max_profit, M[i] - prices[i]);
        
        return max_profit; 


    if __name__ == "__main__":
       test = [7,1,5,3,6,4]
       print("The max profit is " + str(maxProfit(test)))