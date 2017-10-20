# -*- coding:utf-8 -*-
# __author__=''
from math import sqrt
class Solution(object):
    def numberOfBoomerangs(self, points):
        ans = 0
        for i in range(len(points)):
            D = dict()
            for j in range(len(points)):
                if i == j:
                    continue
                distance = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                if distance in D:
                    ans += D[distance]
                    D[distance] += 2
                else:
                    D[distance] = 2
        return ans




if __name__ == '__main__':
    a = Solution()
    print (a.numberOfBoomerangs([[0,0],[0,0]]))