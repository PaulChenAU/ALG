# -*- coding:utf-8 -*-
# __author__=''
import sys
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for index,item in enumerate(s):
            if item not in dic:
                dic[item] = index
            elif item in dic:
                dic[item] = -1
        print (dic)
        min = sys.maxsize
        for i in dic:
            if dic[i] >= 0 and dic[i] != -1:
                if dic[i] < min:
                    min = dic[i]
        return min if min != sys.maxsize else -1


if __name__ == '__main__':
    a = Solution()
    print (a.firstUniqChar("loveleetcode"))