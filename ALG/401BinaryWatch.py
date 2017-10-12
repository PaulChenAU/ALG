# -*- coding:utf-8 -*-
# __author__=''
'''

Good Solution from Stefan
up
'''
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ["%d:%02d" % (i,j) for i in range(0,12) for j in range(0,60) if (bin(i)+bin(j)).count('1') == num]



if __name__ == '__main__':
    #print ([i+j for i in range(10) for j in range(5) if i == 9 and j == 2])
    #print (['%d' % m for m in range(60)])
    a = Solution()
    print (a.readBinaryWatch(0))

