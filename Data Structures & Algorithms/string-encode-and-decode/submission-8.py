class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        l = ""
        while i < len(s):
            if s[i] != '#':
                l += s[i]
                i += 1
                continue
            
            lx = int(l)
            l = ""
            
            res.append(s[i + 1:i + 1 + lx])
            i += 1 + lx

        return res


        
