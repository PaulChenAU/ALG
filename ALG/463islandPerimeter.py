# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        row,col = len(grid),len(grid[0])
        visited = [[0 for i in range(col)] for j in range(row)]
        ans = 0
        s = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ans += 4
                    if j-1>=0:
                        if grid[i][j-1]:
                            ans -= 1
                    if i-1>=0:
                        if grid[i-1][j]:
                            ans -= 1
                    if i+1<row:
                        if grid[i+1][j]:
                            ans -= 1
                    if j+1<col:
                        if grid[i][j+1]:
                            ans -= 1
        return ans


if __name__ == '__main__':
    a = Solution()
    print (a.islandPerimeter([[0,0,0],[0,0,1]]))


'''
 1 - 4
 2 - 6
 3 - 8
 4 -


'''