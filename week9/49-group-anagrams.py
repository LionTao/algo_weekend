"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket=dict()
        for s in strs:
            curr = list(s)
            curr.sort()
            curr=str(curr)
            if curr in bucket:
                bucket[curr].append(s)
            else:
                bucket[curr]=[s]
        res=[]
        for _,v in bucket.items():
            res.append(v)
        return res