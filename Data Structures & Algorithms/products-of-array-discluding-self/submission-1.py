class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1]
        for i in range(1, len(nums)):
            product = forward[-1] * nums[i - 1]
            forward.append(product)

        backward = [1]
        for i in range(len(nums) - 2, -1, -1):
            prod = backward[-1] * nums[i + 1]
            backward.append(prod)

        out = []
        for i in range(len(forward)):
            out.append(forward[i] * backward[len(backward) - i - 1])
        
        return out