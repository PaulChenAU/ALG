# -*- coding:utf-8 -*-
# __author__=''
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
def mergeTwoLists(l1,l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    else:
        if l1.val < l2.val:
            m = l1
            start = m
            l1 = l1.next
        else:
            m = l2
            start = m
            l2 = l2.next
        while True:
            if l1 is None:
                m.next = l2
                return start
            elif l2 is None:
                m.next = l1
                return start
            elif l1 is None and l2 is None:
                return start
            else:
                if l1.val < l2.val:
                    m.next = l1
                    m = m.next
                    l1 = l1.next
                else:
                    m.next = l2
                    m = m.next
                    l2 = l2.next

if __name__ ==  '__main__':
    for i in range(0,10):
        locals()['l'+str(i)] = ListNode(i)
    for i in range(0,8,2):
        locals()['l'+str(i)].next=locals()['l'+str(i+2)]
    for i in range(1, 9, 2):
        locals()['l'+str(i)].next=locals()['l'+str(i+2)]
    i = 0
    print (l0.val,l1.val)
    print (l0.next.val)
    #print (mergeTwoLists(l0,l1))
    x = mergeTwoLists(l0,l1)
    #print (x.val)
    while (x!=None):
        print (x.val)
        x=x.next
    #while x != None:
     #   print (x.val)
      #  x = x.next
