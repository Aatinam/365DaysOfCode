#Day 3 of 365 Days of Code
#Problem Source: https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/

#Problem Statement: Given an integer array nums of unique elements, return all possible subsets (the power set).
#The solution set must not contain duplicate subsets. Return the solution in any order.


class Solution:
    def subsets(self, nums) :
        ans = [[]];
        
        def allSubsets(arr, k, nums):
            length = len(nums);
            if k < length:
                new_arr = arr;
                for i in range(k, length):                    
                    new_arr.append(nums[i]);
                    ans.append(new_arr.copy());
                    allSubsets(new_arr, i+1, nums);
                    new_arr.pop();
        
        allSubsets([], 0, nums);
        return ans;