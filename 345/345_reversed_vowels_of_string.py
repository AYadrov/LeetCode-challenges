# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "hello"
# Output: "holle"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1

        def isvowel(s):
            return s in "aeiouAEIOU"

        s = list(s)
        while(end > start):
            if isvowel(s[start]):
                if isvowel(s[end]):
                    temp = s[end]
                    s[end] = s[start]
                    s[start] = temp
                    end -= 1
                    start += 1
                else:
                    end -= 1
            else:
                start += 1
        return "".join(s)