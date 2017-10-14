# -*- coding:utf-8 -*-
# __author__=''
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = []
        ans = []
        pre = root
        while len(s)>0 or pre:
            if pre.left:
                s.append(pre)
                pre = pre.left
            else:
                ans.append(pre.val)
                pre = pre.right
                while not pre and len(s)>0:
                    pre = s.pop()
                    ans.append(pre.val)
                    pre = pre.right
        min = abs(ans[1] - ans[0])
        k = 2
        while k < len(ans):
            if abs(ans[k] - ans[k-1])<min:
                min = abs(ans[k] - ans[k-1])
            k += 1
        return min




if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    l = Solution()
    print (l.getMinimumDifference(a))
    k = []
    print ()
