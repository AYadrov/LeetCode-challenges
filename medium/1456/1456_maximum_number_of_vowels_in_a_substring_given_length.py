# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

# Example 2:
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

# Example 3:
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isvowel(x):
            return 1 if x in "aeiou" else 0

        max_cnt = sum(map(isvowel, s[:k]))
        cnt = max_cnt
        for i in range(k, len(s)):
            cnt = cnt + isvowel(s[i]) - isvowel(s[i-k])
            if cnt > max_cnt:
                max_cnt = cnt
        return max_cnt