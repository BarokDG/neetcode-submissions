class Solution:
    def isPalindrome(self, s: str) -> bool:
        par = ''

        for char in s:
            if char.isalnum():
                par += char.lower()

        return par == par[::-1]