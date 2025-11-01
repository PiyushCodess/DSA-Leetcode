class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        n_cols = len(matrix[0])
        heights = [0] * (n_cols + 1)
        max_area = 0

        for row in matrix:
            for i in range(n_cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            stack = []
            for i in range(n_cols + 1):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area
