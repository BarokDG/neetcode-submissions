class Solution:
    def isValid(self, s: str) -> bool:
        op = "([{"
        pairs = {
            ')' : '(',
            ']': '[',
            '}': '{'
        }

        st = []
        for c in s:
            if c in op:
                st.append(c)
                continue
            
            top = st.pop() if st else None
            if pairs[c] != top:
                return False

        return len(st) == 0