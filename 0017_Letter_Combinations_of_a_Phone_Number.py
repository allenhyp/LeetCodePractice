class Solution:
    def __init__(self):
        self.dtl = {'1': ['*'],
               '2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z'],
               '0': [' ']}


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        result = ['']
        for digit in digits:
            temp = result
            del result
            result = []
            for t in temp:
                for letter in self.dtl[digit]:
                    result.append(t + letter)
        return result


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def recursive(index, curr):
            if index == len(digits):
                return curr
            if not curr:
                return recursive(index + 1, map[digits[index]])
            next = []
            for c in curr:
                for p in map[digits[index]]:
                    next.append(c + p)
            return recursive(index + 1, next)
        
        return recursive(0, [])
