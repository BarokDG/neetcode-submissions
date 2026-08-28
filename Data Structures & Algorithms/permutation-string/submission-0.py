class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}

        for c in s1:
            count[c] = count.get(c, 0) + 1

        n = len(s1)
        window_count = {}
        for i in range(len(s2) - n + 1):
            if i == 0:
                window = s2[:n]
                for c in window:
                    window_count[c] = window_count.get(c, 0) + 1
            else:
                window_count[s2[i - 1]] -= 1
                window_count[s2[i + n - 1]] = window_count.get(s2[i + n - 1], 0) + 1

            for c in count:
                if count[c] != window_count.get(c, 0):
                    break
            else:
                return True

        return False
