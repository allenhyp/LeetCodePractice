class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters = sorted(letters, key=lambda x: str(x.split()[1:]) + x.split()[0])
        return letters + digits


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def transferLog2Key(log):
            left, right = log.split(' ', 1)
            if right[0].isdigit():
                return (1, )
            else:
                return (0, right, left)
        return sorted(logs, key=transferLog2Key)
