#Day 13 of 365 days of code
#Link for leetcode: https://leetcode.com/problems/longest-increasing-subsequence/

#Problem Statement : Given an integer array nums, return the length of the longest strictly increasing subsequence.
#A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing 
#the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].


class Solution:
    def lengthOfLIS_Solution1(self, nums):
        #Solution 1 Runtime O(n^2)
        if len(nums) <=1:
            return len(nums);
        
        dp = [0]* len(nums);
        max_subsequence_len = 0
        
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j])
                    
            dp[i] +=1;
            max_subsequence_len = max(max_subsequence_len, dp[i])
        
        return max_subsequence_len;


    def lengthOfLIS_Solution2(self, nums):
        ##Solution 2 runtime O(nlogn)
        if len(nums) <= 1:
            return len(nums);
        
        dp = [];
        dp.append(nums[0]);
        
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                start = 0;
                end = len(dp);
                while(start != end):
                    mid = start + ((end-start)//2);
                    if nums[i] > dp[mid]:
                        start = mid;
                    else: #nums[i] <= dp[mid]
                        if (mid - 1 < 0 or dp[mid-1] < nums[i]): # can't go any more left
                            dp[mid] = nums[i]
                            break;
                        end = mid;
        return len(dp);