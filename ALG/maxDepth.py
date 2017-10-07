# -*- coding:utf-8 -*-
# __author__=''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        return 1 + max(maxDepth(root.left),maxDepth(root.right))
