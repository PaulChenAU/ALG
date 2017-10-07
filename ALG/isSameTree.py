# -*- coding:utf-8 -*-
# __author__=''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return p is q

if __name__ == '__main__':
    p = TreeNode(3)
    q = TreeNode(3)
    print (p.val,q.val,p == q)
