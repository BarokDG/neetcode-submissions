class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        l, r = 0, 0
        longest = 0

        while r < len(s):
            curr = s[r]
            if curr not in sub:
                sub.add(curr)
                r += 1
                continue
            
            longest = max(longest, len(sub))

            while curr in sub:
                sub.remove(s[l])
                l += 1
        
        return max(longest, len(sub))