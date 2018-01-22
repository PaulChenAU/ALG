# -*- coding:utf-8 -*-
# __author__=''
# python did well numerical calculation than java
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 0 or len(words) == 1:
            return 0
        d = {}
        for word in words:
            mask = 0
            for char in set(word):
                mask |= (1 << ord(char) - 97)
            d[mask] = max(d.get(mask,0), len(word))
        return max([d[x] * d[y] for x in d for y in d if x & y ==0] or [0])

if __name__ == '__main__':
    a = Solution()
    print(a.maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]))
    mask = 0
    for c in set("deeede"):
        mask |= (1<< ord(c)-97)