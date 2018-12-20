class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = re.split('\W+', paragraph)
        dic = {}
        for w in words:
            w = w.lower()
            if w not in banned:
                if w not in dic.keys():
                    dic[w] = 1
                else:
                    dic[w] += 1
        max_feq = 0
        res = ''
        for key, val in iter(dic.items()):
            if val > max_feq:
                max_feq = val
                res = key
        return res
