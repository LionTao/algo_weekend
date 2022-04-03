"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 3
        a,b,c=1,2,3
        for _ in range(4,n+1):
            a=b
            b=c
            c=a+b
        return c