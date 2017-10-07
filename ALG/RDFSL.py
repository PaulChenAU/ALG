# -*- coding:utf-8 -*-
# __author__=''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        ans = head
        while head.next is not None:
            if head.next.val == head.val:
                if head.next.next is None:
                    head.next = None
                else:
                    head.next = head.next.next
            elif head.next.val != head.val:
                head = head.next
        return ans

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    d = ListNode(1)
    a.next = b
    b.next = d
    c = Solution()
    print (a.val,a.next.val)
    print ("函数运行结果:",c.deleteDuplicates(a).val)
    while a is not None:
        print (a.val,)
        a = a.next