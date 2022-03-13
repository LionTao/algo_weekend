"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

要求: 用分治实现
"""
from typing import List,Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    思路: 递归调用合并
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        n = len(lists) #记录子链表数量
        return self.mergeSort(lists, 0, n - 1) #调用归并排序函数

    def mergeSort(self, lists: List[ListNode], l: int, r: int) -> ListNode:
        if l == r:
            return lists[l]
        m = (l + r) // 2
        L = self.mergeSort(lists, l, m) #循环的递归部分
        R = self.mergeSort(lists, m + 1, r)
        return self.mergeTwoLists(L, R) #调用两链表合并函数

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0) #构造虚节点
        move = dummy #设置移动节点等于虚节点
        while l1 and l2: #都不空时
            if l1.val < l2.val:
                move.next = l1 #移动节点指向数小的链表
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2 #连接后续非空链表
        return dummy.next #虚节点仍在开头