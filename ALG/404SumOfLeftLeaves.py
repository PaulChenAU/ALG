# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        ------For Debug------
        if root:
            print ("当前结点"+str(root.val))
        else:
            print ("当前结点为空")
        '''
        if root is None:
            return 0
        if root.left and root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        '''
            1
          2   3
        4    5
          6
        '''


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    a.left = b
    a.right = c
    b.left = d
    c.left = e
    d.right = f
    f.left = g
    l = Solution()
    print (l.sumOfLeftLeaves(a))
    print (a.val)
    print (a.val)
