# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 0 or len(words) == 1:
            return 0
        sort_words = sorted(words, key=lambda x: len(x))
        diff = []
        for i in range(len(words) - 1):
            diff.append([])
            for j in range(i + 1, len(words)):
                if len(list(set(list(words[i])))) + len(list(set(list(words[j])))) == len("".join(list(set(list(words[i] + words[j]))))):
                    diff[i].append(len(words[i]) * len(words[j]))
        for i in range(len(diff)):
            diff[i] = max(diff[i]) if diff[i] != [] else 0
        return max(diff)

if __name__ == '__main__':
    a = Solution()
    print(a.maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]))
