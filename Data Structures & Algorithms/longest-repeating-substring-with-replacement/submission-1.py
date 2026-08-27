class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            curr = s[r]
            mp[curr] = mp.get(curr, 0) + 1

            window = r - l + 1
            if window - max(mp.values()) > k:
                mp[s[l]] -= 1
                l += 1
            else:
                longest = max(longest, window)
        
        return longest
