class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen_chars=set()
        longest=0
        left=0

        for right in range(len(s)):

            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left+=1

            seen_chars.add(s[right])

            if (right-left+1)>longest:
                longest= right-left+1

        return longest
        