# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def generate(self, numRows):
        list1 = [1]
        list2 = [1,1]
        anslist = []
        if numRows == 0:
            return anslist
        if numRows == 1:
            anslist.append(list1)
            return anslist
        if numRows == 2:
            anslist.append(list1)
            anslist.append(list2)
            return anslist
        oldlist = list2
        anslist.append(list1)
        anslist.append(list2)
        for k in range(2,numRows):
            newlist = []
            newlist.append(1)
            old = 0
            for i in range(0,len(oldlist)-1):
                newlist.append(oldlist[old]+oldlist[old+1])
                old += 1
            newlist.append(1)
            oldlist = newlist
            anslist.append(newlist)
        return anslist


if __name__ == '__main__':
    a = Solution()
    print (a.generate(5))