# -*- coding:utf-8 -*-
# __author__=''
import copy
import time
import arrow

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
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                v = []
                for vi in range(len(matrix)):
                    v.append([])
                    for vj in range(len(matrix[vi])):
                        v[vi].append(0)
                self.dfs(i, j, 1, matrix, v)
        return self.max

    def dfs(self, i, j, ans, matrix, v):
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
    matrix = [[7, 7, 11, 19, 17, 13, 15, 7, 1, 6, 15, 6, 19, 10, 13, 3, 5, 16, 10, 6, 0, 9, 14],
              [17, 6, 9, 19, 7, 7, 8, 17, 13, 0, 8, 2, 10, 9, 9, 14, 13, 15, 14, 3, 10, 15, 12],
              [12, 14, 18, 1, 12, 16, 19, 17, 14, 0, 14, 9, 0, 4, 7, 14, 8, 6, 15, 14, 15, 16, 6],
              [18, 9, 7, 15, 3, 6, 15, 16, 15, 5, 6, 19, 12, 18, 12, 19, 5, 5, 14, 19, 1, 17, 6],
              [14, 16, 15, 6, 15, 8, 6, 7, 15, 9, 5, 6, 5, 10, 4, 1, 6, 16, 7, 3, 4, 3, 19],
              [17, 1, 11, 7, 10, 12, 0, 12, 0, 12, 1, 1, 5, 1, 7, 15, 17, 16, 8, 17, 0, 19, 7],
              [16, 8, 2, 19, 18, 17, 0, 11, 17, 9, 14, 5, 19, 12, 15, 11, 0, 13, 9, 7, 15, 8, 0],
              [19, 10, 2, 6, 17, 6, 11, 15, 5, 12, 19, 18, 9, 3, 9, 4, 10, 6, 10, 5, 9, 5, 9],
              [13, 17, 0, 0, 10, 5, 0, 18, 13, 6, 7, 16, 7, 18, 11, 15, 17, 1, 2, 11, 8, 16, 17],
              [18, 11, 16, 15, 9, 6, 9, 2, 4, 9, 3, 17, 2, 18, 15, 0, 11, 16, 11, 2, 17, 17, 5],
              [0, 2, 7, 14, 12, 12, 18, 2, 17, 0, 2, 12, 17, 2, 17, 19, 9, 9, 17, 13, 0, 11, 17],
              [9, 8, 11, 12, 4, 10, 6, 2, 4, 10, 18, 18, 4, 8, 2, 14, 13, 18, 12, 9, 19, 14, 4],
              [11, 1, 10, 13, 14, 10, 7, 10, 11, 19, 4, 3, 14, 17, 13, 11, 0, 9, 8, 14, 9, 9, 11],
              [12, 15, 6, 16, 5, 11, 12, 15, 0, 10, 9, 2, 19, 11, 6, 19, 5, 0, 17, 6, 18, 6, 3],
              [5, 0, 18, 18, 11, 11, 10, 10, 17, 11, 14, 10, 0, 15, 9, 12, 4, 10, 0, 17, 12, 19, 1],
              [18, 12, 6, 12, 15, 12, 16, 19, 2, 8, 8, 9, 1, 18, 19, 14, 14, 6, 16, 17, 15, 1, 10],
              [3, 14, 0, 6, 7, 8, 5, 9, 8, 2, 18, 10, 19, 17, 10, 18, 14, 17, 8, 1, 7, 1, 1],
              [12, 13, 15, 2, 12, 14, 3, 4, 15, 16, 11, 17, 0, 1, 1, 16, 14, 3, 5, 17, 4, 14, 7]]

    s = Solution()
    begin = time.time()
    print(arrow.get(begin))
    print(s.longestIncreasingPath(matrix))
    end = time.time()
    print(arrow.get(end))

