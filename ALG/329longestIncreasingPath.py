# -*- coding:utf-8 -*-
# __author__=''
import copy
class Solution(object):

    def __init__(self):
        self.max = 0

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                v = []
                for vi in range(len(matrix)):
                    v.append([])
                    for vj in range(len(matrix[vi])):
                        v[vi].append(0)
                self.dfs(i,j,1,matrix,v)
        return self.max


    def dfs(self,i, j, ans, matrix, v):
        if ans > self.max:
            self.max = ans
        pv = copy.deepcopy(v)
        pv[i][j] = 1
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if i + dx < len(matrix) and i + dx >= 0 and j + dy < len(matrix[i + dx]) and j + dy >= 0 and pv[i + dx][
                            j + dy] != 1 and dx != dy and dx != -dy and matrix[i + dx][j + dy] > matrix[i][j]:
                    self.dfs(i + dx, j + dy, ans + 1, matrix, pv)

if __name__ == '__main__':
    matrix = [
        [7,8,9],
        [9,7,6],
        [7,2,3]
    ]

    s = Solution()
    print (s.longestIncreasingPath(matrix))