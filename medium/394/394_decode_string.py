# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], 
# where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; 
# there are no extra white spaces, square brackets are well-formed, etc. 
# Furthermore, you may assume that the original data does not contain 
# any digits and that digits are only for those repeat numbers, k. 
# For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

class Solution:
    def decodeString(self, s: str) -> str:
        def parse(s):
            s_new = ''
            number = 0
            i = 0
            while i < len(s):
                if s[i].isdigit():
                    number = number*10 + int(s[i])
                elif s[i] == '[':
                    parsed_str, shift = parse(s[i+1:])
                    i += shift + 1
                    s_new += parsed_str*number
                    number = 0
                elif s[i] == ']':
                    return s_new, i
                else:
                    s_new += s[i]
                i+=1
            return s_new, i     
        return parse(s)[0]