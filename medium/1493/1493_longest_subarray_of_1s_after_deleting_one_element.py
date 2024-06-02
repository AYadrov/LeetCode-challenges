# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

# Example 3:
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.

class Solution:
    # Two pointer solution
    def longestSubarray(self, nums: List[int]) -> int:
        t = 1  # counter of zeros between R and L pointers
        L = 0
        max_ = 0

        for R in range(len(nums)):
            if nums[R] == 0:
                t-=1
            
            # Calculate max only when R is ahead of L
            if t >= 0:
                max_ = R-L+min(t,0)
            if t < 0:
                if nums[L] == 0:
                    t+=1
                L+=1
        return max_