class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1l, v2l = version1.split('.'), version2.split('.')
        for i in range(max(len(v1l), len(v2l))):
            v1 = int(v1l[i]) if i < len(v1l) else 0
            v2 = int(v2l[i]) if i < len(v2l) else 0
            if v1 != v2:
                return 1 if v1 > v2 else -1
        return 0
