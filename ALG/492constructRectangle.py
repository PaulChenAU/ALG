# -*- coding:utf-8 -*-
# __author__=''
import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if area == 0:
            return [0,0]
        a = int(math.sqrt(area))
        while area % a != 0:
            a -= 1
        return [int(area/a),int(a)]


if __name__ == '__main__':
    a = Solution()
    print (a.constructRectangle(0))