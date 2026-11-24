class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < len(longest) and j < len(strs[i]) and longest[j] == strs[i][j]:
                j += 1
            longest = longest[:j]

        return longest
