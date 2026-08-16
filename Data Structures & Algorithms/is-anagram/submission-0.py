class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            c = s[i]
            countS[c] = 1 + countS.get(c, 0)

            c = t[i]
            countT[c] = 1 + countT.get(c, 0)

        if len(countS) != len(countT):
            return False
        
        for k in countS.keys():
            if countS[k] != countT.get(k, 0):
                return False
        
        return True