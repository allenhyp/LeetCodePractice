class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        map = collections.defaultdict(list)
        for s in strings:
            key = ()
            for i in range(len(s)-1):
                key += ((ord(s[i+1])-ord(s[i])) % 26, )
            map[key].append(s)
        return list(map.values())
