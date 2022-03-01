"""
Проверить дерево на симметричность:
https://leetcode.com/problems/symmetric-tree/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(node1, node2):

            if node1 is None and node2 is None:
                return True

            if node1 is not None and node2 is not None and node1.val == node2.val:
                return helper(node1.left, node2.right) and helper(node1.right, node2.left)

            return False

        return helper(root.left, root.right)
