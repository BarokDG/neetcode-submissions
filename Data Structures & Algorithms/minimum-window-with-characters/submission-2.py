class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        min_sub = ""

        t_count, s_count = {}, {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
            s_count[c] = 0

        l = 0
        have = 0
        need = len(t)
        for r in range(len(s)):
            curr = s[r]
            if curr not in t:
                continue

            s_count[curr] = s_count.get(curr, 0) + 1
            if s_count[curr] <= t_count[curr]:
                have += 1

            while have == need:
                curr_sub = s[l:r+1]
                if not min_sub or len(min_sub) > len(curr_sub):
                    min_sub = curr_sub

                if s[l] in t:
                    s_count[s[l]] -= 1

                    if s_count[s[l]] < t_count[s[l]]:
                        have -= 1

                l += 1

        return min_sub