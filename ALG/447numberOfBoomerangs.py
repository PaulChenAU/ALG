# -*- coding:utf-8 -*-
# __author__=''
from math import sqrt
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if points is None or len(points) < 3:
            return 0
        ans = 0
        for i in range(len(points)):
            for j in range(len(points)):
                for k in range(len(points)):
                    dij = sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
                    dik = sqrt((points[i][0]-points[k][0])**2 + (points[i][1]-points[k][1])**2)
                    if dij == dik and i != j and j != k and i != k:
                        print(i, j, k, " and ", dij, dik)
                        ans += 1
        return ans




if __name__ == '__main__':
    a = Solution()
    print (a.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))