class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i in range(len(heights)):
            height = heights[i]

            new_index = i
            while stack and stack[-1][1] >= height:
                start_index, h = stack.pop()
                area = h * (i - start_index)
                max_area = max(area, max_area)

                new_index = start_index

            stack.append((new_index, height))

        for (i, h) in stack:
            area = (len(heights) - i) * h
            max_area = max(area, max_area)

        return max_area


