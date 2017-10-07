# -*- coding:utf-8 -*-
# __author__=''
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        a,b = head,head
        while True:
            if b is None:
                return False
            a = a.next
            for i in range(0,2):
                b = b.next
                if b is None:
                    return False
            if a == b:
                return True

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(4)
    c = ListNode(5)
    a.next = b
    b.next = c
    c.next = a
    so = Solution()
    print (so.hasCycle(a))
    print ()