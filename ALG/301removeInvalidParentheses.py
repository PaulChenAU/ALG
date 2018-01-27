# -*- coding:utf-8 -*-
# __author__=''

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def judge(s):
            ns = ""
            for i,c in enumerate(s):
                if c == "(" or c == ")":
                    ns += c
            while '()' in ns:
                ns = ns.replace('()','')
            return not ns

        ans_set = {s}
        ns = ""
        for i, c in enumerate(s):
            if c != "(" and c != ")":
                ns += c
        z_ans_set = {ns}
        while True:
            valid = list(filter(judge, ans_set))
            if valid:
                return valid
            new_ans_set = set()
            for s in ans_set:
                for i in range(len(s)):
                    new_ans_set.add(s[:i] + s[i+1:])
            ans_set = new_ans_set
            if len(ans_set) == 1:
                return list(z_ans_set)




if __name__ == '__main__':
    a = Solution()
    print (a.removeInvalidParentheses("nn"))
    s = "(())"
    print(s)
