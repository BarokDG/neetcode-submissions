class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for i in range(1, len(strs)):
            curr = strs[i]
            j = 0
            while j < min(len(longest), len(curr)) and longest[j] == curr[j]:
                j += 1
            longest = longest[:j]

        return longest
