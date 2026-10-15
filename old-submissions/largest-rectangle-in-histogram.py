class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        count = 0

        for i in range(0, len(heights)):
            while (len(stack) != 0 and heights[i] < heights[stack[-1]]):
                height = heights[stack.pop()]
                nse = i
                pse = -1
                if (len(stack) != 0):
                    pse = stack[-1]
                
                count = max(count, (nse-pse-1) * height)
            stack.append(i)

        while (len(stack) != 0):
            nse = len(heights)
            height = heights[stack.pop()]
            pse = -1
            if (len(stack) != 0):
                pse = stack[-1]
            
            count = max(count, (nse-pse-1) * height)

        return count
