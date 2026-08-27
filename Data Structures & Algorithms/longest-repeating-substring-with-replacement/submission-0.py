class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            curr = s[r]
            mp[curr] = mp.get(curr, 0) + 1

            freq = self.getMostFrequentCharacterCount(mp)
            window = r - l + 1
            if window - freq > k:
                mp[s[l]] -= 1
                l += 1
            else:
                longest = max(longest, window)
        
        return longest

    
    def getMostFrequentCharacterCount(self, mp: dict[str, int]):
        most_freq = 0

        for key in mp:
            most_freq = max(most_freq, mp[key])

        return most_freq