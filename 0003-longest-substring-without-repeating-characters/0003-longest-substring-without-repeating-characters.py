class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen_chars={}
        longest=0
        left=0

        for right in range(len(s)):

            if s[right] in seen_chars:
                left=max (seen_chars[s[right]]+1, left)

            seen_chars[s[right]]=right

            if (right-left+1)>longest:
                longest = right-left+1

        return longest
        