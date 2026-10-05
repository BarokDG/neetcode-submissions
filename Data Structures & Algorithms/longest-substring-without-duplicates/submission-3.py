class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = 0

        l = 0
        seen = {}
        for r in range(len(s)):
            while s[r] in seen:
                del seen[s[l]]
                l += 1

            seen[s[r]] = 1
            max_substring = max(r - l + 1, max_substring)

        return max_substring