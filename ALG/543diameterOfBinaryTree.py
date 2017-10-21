# -*- coding:utf-8 -*-
# __author__=''
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = []
        ans = []
        pre = root
        while len(s) > 0 or pre:
            if pre.left:
                s.append(pre)
                pre = pre.left
            else:
                ans.append(self.dfs(pre))
                pre = pre.right
                while not pre and len(s) > 0:
                    pre = s.pop()
                    ans.append(self.dfs(pre))
                    pre = pre.right
        return max(ans)-1

    def dfs(self,root):
        if

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    d.right = e
    l = Solution()
    #print (a)
    print (l.dfs(a))
    print(l.dfs(b))
    print(l.dfs(c))
    print(l.dfs(d))
    print (l.diameterOfBinaryTree(a))

'''
      a
    b   c
  d
   e




'''