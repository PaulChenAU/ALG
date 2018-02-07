# -*- coding:utf-8 -*-
# __author__=''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rootNotInclude, rootIncluded = self.traverse(root)
        return max(rootNotInclude, rootIncluded)


    def traverse(self, root):
        if root is None:
            return 0,0

        tl, tr = self.traverse(root.left), self.traverse(root.right)

        rootNotInclude = max(tl) + max(tr)
        rootIncluded = root.val + tl[0] + tr[0]

        return rootNotInclude, rootIncluded




    def rob2(self,root):
        if root is None:
            return 0
        val = 0
        if root.left:
            val += self.rob2(root.left.left) + self.rob2(root.left.right)
        if root.right:
            val += self.rob2(root.right.left) + self.rob2(root.right.right)

        return max(val + root.val, self.rob2(root.left) + self.rob2(root.right))

    def test(self):
        return 1,2
if __name__ == '__main__':
    s = Solution()
    a = TreeNode(3)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left, a.right = b,c
    d = TreeNode(3)
    e = TreeNode(1)
    b.right = d
    c.right = e
    print(s.rob(a))

    s2 = Solution()
    t1 = TreeNode(4)
    t2 = TreeNode(1)
    t3 = TreeNode(2)
    t4 = TreeNode(3)
    t1.left, t2.left, t3.left = t2, t3, t4
    print(s2.rob2(t1))

    s3 = Solution()
    print(s3.rob(t1))