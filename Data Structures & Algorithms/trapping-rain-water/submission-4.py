class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]
        for i in range(1, len(height)):
            left = max(max_left[i - 1], height[i - 1])
            max_left.append(left)
        
        max_right = [0]
        reversed_height = height[::-1]
        for i in range(1, len(reversed_height)):
            right = max(max_right[i - 1], reversed_height[i - 1])
            max_right.append(right)
        max_right = max_right[::-1]

        water = 0
        for i in range(len(height)):
            new_water = min(max_left[i], max_right[i]) - height[i]
            water += max(0, new_water)

        return water
