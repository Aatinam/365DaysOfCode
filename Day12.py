#Day 12 of 365 days of code
#Link for leetcode: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

#Problem Statement : Given an array of integers nums and an integer target, return indices of the two numbers such that they 
#add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.


class Solution:
    def twoSum( nums, target):
        dict = {}
        for i in range(0, len(nums)):
            dict[nums[i]] = i;
            
        for i in range(0, len(nums)):
            remainder = target - nums[i];
            if remainder in dict and dict[remainder] != i:
                return [i, dict[remainder]]

if __name__ == "__main__":
  sol = Solution();
  print(sol.twoSum([3,2,4], 6));
