# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = sum(nums[:k])
        avg = max_avg
        for i in range(k, len(nums)):
            avg += nums[i]
            avg -= nums[i-k]
            if avg > max_avg:
                max_avg = avg
        return max_avg/k