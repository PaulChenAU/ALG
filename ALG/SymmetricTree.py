# -*- coding:utf-8 -*-
# __author__=''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        def isEqual(node1,node2):
            if not node1 and not node2:
                return True
            if node1 and node2 and node1.val == node2.val:
                return isEqual(node1.left,node2.right) and isEqual(node1.right,node2.left)
            return False
        return isEqual(root,root)

if __name__ == '__main__':
    a = TreeNode(1)
    c = TreeNode(3)
    a.left = c
    b = Solution()
    print (b.isSymmetric(c))