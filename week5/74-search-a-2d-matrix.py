"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
"""
from typing import List
class Solution:
    """
    看成一个左下或者右上开始的二叉搜索树即可
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        row,col = m-1,0

        while row>=0 and col<n:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                col+=1
            else:
                row-=1
        return False