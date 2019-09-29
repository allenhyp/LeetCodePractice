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
