class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        result = 0
        for w in words:
            if len(w) <= len(S):
                i, j = 0, 0
                while j < len(S):
                    if i < len(w) and w[i] == S[j]:
                        i += 1
                    elif j > 0 and S[j] == S[j - 1] and j + 1 < len(S) and S[j] == S[j + 1]:
                        j += 1
                    elif not (j > 1 and S[j] == S[j - 1] and S[j] == S[j - 2]):
                        break
                    j += 1
                if (i == len(w) and j == len(S)):
                    result += 1
        return result

def main():
    my_solution = Solution()
    print(my_solution.expressiveWords("heeellooo", ["helo","heello","hello"]))


if __name__ == "__main__":
    main()
