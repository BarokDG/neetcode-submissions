class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        longest = 0

        l = 0
        for r in range(len(s)):
            curr = s[r]
            mp[curr] = mp.get(curr, 0) + 1

            if (r - l + 1) - max(mp.values()) > k:
                mp[s[l]] -= 1
                l += 1
    
            longest = max(longest, r - l + 1)
        
        return longest
