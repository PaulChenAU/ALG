# -*- coding:utf-8 -*-
# __author__=''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        elif head.next is None:
            return head
        odd , ans , even, even_head = head, head, head.next, head.next
        while even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
            if even is None:
                break
        odd.next = even_head
        return ans


if __name__ == '__main__':
    pass

