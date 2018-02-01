# -*- coding:utf-8 -*-
# __author__=''
class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.SumMatrix = []
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
            self.SumMatrix = [[0] * n for i in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == 0 and j == 0:
                        self.SumMatrix[i][j] = matrix[i][j]
                    elif i == 0:
                        self.SumMatrix[i][j] = self.SumMatrix[i][j - 1] + self.matrix[i][j]
                    elif j == 0:
                        self.SumMatrix[i][j] = self.SumMatrix[i - 1][j] + self.matrix[i][j]
                    else:
                        self.SumMatrix[i][j] = self.SumMatrix[i - 1][j] + self.SumMatrix[i][j - 1] - \
                                               self.SumMatrix[i - 1][j - 1] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.SumMatrix[row2][col2]
        elif row1 == 0:
            return self.SumMatrix[row2][col2] - self.SumMatrix[row2][col1-1]
        elif col1 == 0:
            return self.SumMatrix[row2][col2] - self.SumMatrix[row1-1][col2]
        else:
            return self.SumMatrix[row2][col2] - self.SumMatrix[row1 - 1][col2] - self.SumMatrix[row2][col1 - 1] + \
                   self.SumMatrix[row1 - 1][col1 - 1]


            # Your NumMatrix object will be instantiated and called as such:
            # obj = NumMatrix(matrix)
            # param_1 = obj.sumRegion(row1,col1,row2,col2)


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    nm = NumMatrix(matrix)
    print(nm.sumRegion(2, 1, 4, 3))
    print(nm.sumRegion(1, 1, 2, 2))
    print(nm.sumRegion(1, 2, 2, 4))
