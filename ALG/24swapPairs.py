# -*- coding:utf-8 -*-
# __author__=''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = head
        head = head.next
        pre.next = head.next
        head.next = pre
        ans = head
        while pre.next:
            head = pre.next
            if head.next:
                pre.next = head.next
                head.next = head.next.next
                pre.next.next = head
                pre = head
            else:
                pre = pre.next
        return ans


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    ans = Solution()
    print (ans.swapPairs(a).next.next.val)