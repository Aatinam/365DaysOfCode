#Day 29 of 365 days of code
#Link for leetcode: https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
#Problem Statement : Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing 
#exactly one element, or false otherwise. If the array is already strictly increasing, return true.

class Solution:

    def canBeIncreasing(self, nums) :
        if len(nums) <= 2:
            return True
        
        seq = [] #Strictly increasing sequence
        seq.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > seq[-1]: 
                seq.append(nums[i])
            else: 
                s = 0
                e = len(seq)-1
                while (s<=e):
                    mid = s+(e-s)//2
                    if seq[mid] < nums[i]:
                        s=mid+1
                    elif seq[mid] >= nums[i]:
                        if mid-1 > s and seq[mid-1] > nums[i]:
                            e = mid-1
                        else: 
                            seq[mid] = nums[i]  
                            break
                            
        if len(nums) - len(seq) <=1:
            return True
        return False            
        


if __name__ == "__main__":
    s = Solution();
    s.canBeIncreasing([1,2,10,5,7])