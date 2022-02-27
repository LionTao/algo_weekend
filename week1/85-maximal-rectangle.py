"""
leetcode-85
给定一个仅包含 0 和 1 , 大小为 rows x cols 的二维二进制矩阵, 找出只包含 1 的最大矩形, 并返回其面积。
"""
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        统计直方图然后单调递增栈
        """
        rows = len(matrix)
        if rows == 0:
            return 0
        columns = len(matrix[0])

        res = 0
        heights = [0]*columns
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c]=="1":
                    heights[c]+=1
                else:
                    heights[c]=0
            res = max(res,self.largestRectangleArea(heights))
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        #单调递增栈
        heights = [-1] + heights + [-1]
        res = 0
        ascend_stack = []        
        for i in range(len(heights)):
            while ascend_stack and heights[ascend_stack[-1]] > heights[i]:
                window_L_height_min_height = heights[ascend_stack.pop(-1)]
                window_L = ascend_stack[-1] + 1
                window_R = i - 1
                cur_area = window_L_height_min_height * (window_R - window_L + 1)
                res = max(res, cur_area)
            ascend_stack.append(i)
        return res