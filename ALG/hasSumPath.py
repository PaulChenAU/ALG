# -*- coding:utf-8 -*-
# __author__=''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if root.left is not None:
            if root.left.val == sum - root.val:
                return True
        if root.right is not None:
            if root.right.val == sum - root.val:
                return True
        if root.val == sum:
            return True
        if root.left is not None:
            self.hasPathSum(root.left,sum-root.val)
        if root.right is not None:
            self.hasPathSum(root.right,sum-root.val)
        return False

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    a.left = b
    b.right = c
    a.right = d
    sol = Solution()
    print(sol.hasPathSum(a,1))