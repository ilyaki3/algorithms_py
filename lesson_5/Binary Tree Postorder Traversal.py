"""
Реализовать обход дерева post-order. Сначала левое, потом правое поддерево, в последнюю очередь корень:
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(node):
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            res.append(node.val)

        if not root:
            return res
        helper(root)
        return res
