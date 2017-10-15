# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        flag = -1 if num < 0 else 1
        bn = list(bin(num)[2:])
        for i in range(len(bn)):
            if bn[i] == '1':
                bn[i] = '0'
            else:
                bn[i] = '1'
        return flag * int("".join(bn),2)







if __name__ == '__main__':
    a = Solution()
    print (a.findComplement(5))