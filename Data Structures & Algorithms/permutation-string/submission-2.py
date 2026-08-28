class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}

        for c in s1:
            count[c] = count.get(c, 0) + 1

        window_count = {}
        n = len(s1)
        for i in range(len(s2) - n + 1):
            if i == 0:
                for c in s2[:n]:
                    window_count[c] = window_count.get(c, 0) + 1
            else:
                window_count[s2[i - 1]] -= 1
                n_c = s2[i + n - 1]
                window_count[n_c] = window_count.get(n_c, 0) + 1

            matches = 0
            for c in count:
                if count[c] == window_count.get(c, 0):
                    matches += 1

            if matches == len(count):
                return True

        return False
