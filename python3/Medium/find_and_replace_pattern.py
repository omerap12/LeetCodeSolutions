# https://leetcode.com/problems/find-and-replace-pattern/description/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """
        A pattern is an Injective function.
        so just check that word[i] = pattern[i] is indeed Injective function
        """
        res = []
        func = {}
        rev_func = {}
        flag = False
        for word in words:
            if len(word) != len(pattern):
                continue
            for i in range(len(word)):
                if word[i] in func.keys():
                    if func[word[i]] != pattern[i]:
                        flag = True
                        break
                func[word[i]] = pattern[i]
                if pattern[i] in rev_func.keys():
                    if rev_func[pattern[i]] != word[i]:
                        flag = True
                        break
                rev_func[pattern[i]] = word[i]
            if not flag:
                res.append(word)
            flag = False
            func.clear()
            rev_func.clear()
        return res
