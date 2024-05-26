# Given an integer array nums, return an array answer such that answer[i] is equal to the product  of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_ = len(nums)
        res = [1] * len_
        start = 0
        end = len_-1
        reduction_l = 1
        reduction_r = 1

        while (end >= 0):
            res[end] *= reduction_r
            res[start] *= reduction_l
            reduction_r *= nums[end]
            reduction_l *= nums[start]
            end -= 1
            start += 1
        return res