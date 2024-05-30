# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L = 0
        R = len(nums)
        t = 0
        cnt = 0
        while(t < len(nums)):
            if nums[t] == 0:
                cnt += 1
            if cnt == k+1:
                R = t
                break
            t += 1

        max_cons = R-L
        cons = 0
        R += 1
        L += 1
        while (R < len(nums)):
            if nums[R] == 0 and nums[L-1] == 0:
                cons = R-L
                if cons > max_cons:
                    max_cons = cons
                R += 1
                L += 1
                continue
            elif nums[L-1] != 0:
                L+=1
            elif nums[R] != 0: 
                R+=1
        cons = R-L
        if cons > max_cons:
            max_cons = cons
        return max_cons
            