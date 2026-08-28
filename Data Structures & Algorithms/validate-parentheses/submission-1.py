class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')' : '(',
            ']': '[',
            '}': '{'
        }

        st = []
        for c in s:
            if c not in pairs:
                st.append(c)
                continue
            
            top = st.pop() if st else None
            if pairs[c] != top:
                return False

        return len(st) == 0