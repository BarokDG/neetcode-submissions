class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i: int):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            print(f"{subset=} one")

            subset.pop()
            dfs(i + 1)


        dfs(0)

        return res
