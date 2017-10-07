# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def getRow(self, rowIndex):
        list = []
        if rowIndex == 0:
            return []
        while rowIndex > 0:
