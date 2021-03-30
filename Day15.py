#Day 15 of 365 days of code
#Link for leetcode:https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

#Problem Statement : Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
#Find all unique triplets in the array which gives the sum of zero.
#Notice that the solution set must not contain duplicate triplets.

##Some notes: I tried so long to find a solution with runtime less than O(n**2) and kept thinking it's impossible. 
##            After, I convinced myself that it can't be less than O(n**2), I kept thinking, I can't possibly have 
##            an O(n**2) algorithm and then use sorting on top of it. The lessons I learned here was 
##            1. Don't be afraid of O(n**2) solutions, sometimes that's the best you can do. 
##            2. Trust your instinct, if you think you need to use sorting or perform other costly operations,
##               it's okay, try them out. Don't write something off, without even trying it, because you think 
##               the intervoewer can't possibly be looking for something like this. 

## There are two tricks to this question, the first is, you need to find three elements x, y, z s.t sum(x,y,z) = 0, if you
##  fix the first element then this is just a two sum problem. The second is if you have used a combination of x and y, don't use it
## again.

class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return [];
        
        solutionSet = [];
        numToIndex = {};
        
        nums.sort();
        for i in range(0, len(nums)):
            numToIndex[nums[i]] = i;
            
        for i in range(0, len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue;
            for j in range(i+1, len(nums)):
                if j>i+1 and nums[j-1] == nums[j]:
                    continue;
                target = -1*(nums[i] + nums[j]);
                if target in numToIndex and numToIndex[target]>j :
                    temp = [nums[i], nums[j], target]
                    solutionSet.append(temp);
        return solutionSet;
                    