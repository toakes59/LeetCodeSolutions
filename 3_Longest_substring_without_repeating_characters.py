class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        max_len = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_dict:
                start = max(start, char_dict[s[end]] + 1)
            char_dict[s[end]] = end
            max_len = max(max_len, end - start + 1)
        
        return max_len
