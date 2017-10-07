# -*- coding:utf-8 -*-
# __author__=''
import queue
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        q = queue.Queue()
        q.put(root)
        pre = 0
        while not q.empty():
            length = q.qsize()
            while length > 0:
                a = q.get()
                if a.left is None and a.right is None:
                    return pre+1
                if a.left:
                    q.put(a.left)
                if a.right:
                    q.put(a.right)
                length -= 1
            pre += 1





if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    a.left = b
    b.right = c
    c.right = d
    sol = Solution()
    print (sol.minDepth(a))