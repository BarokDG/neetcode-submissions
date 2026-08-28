class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        min_sub = ""

        t_count, s_count = {}, {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

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

            if have != need:
                continue

            while have == need:
                if s[l] in t:
                    s_count[s[l]] -= 1

                    if s_count[s[l]] < t_count[s[l]]:
                        have -= 1

                l += 1

            curr_sub = s[l - 1 : r + 1]
            min_sub = min_sub if min_sub and len(min_sub) < len(curr_sub) else curr_sub

        return min_sub