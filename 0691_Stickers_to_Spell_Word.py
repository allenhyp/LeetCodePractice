class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def helper(memo, sticker_maps, target):
            if target in memo:
                return memo[target]
            
            target_map = [0] * 26
            for c in target:
                target_map[ord(c)-ord('a')] += 1

            ret = float('inf')
            for sm in sticker_maps:
                if sm[ord(target[0])-ord('a')] == 0:
                    continue
                s = ''
                for i, v in enumerate(sm):
                    if target_map[i] - v > 0:
                        s += chr(ord('a')+i) * (target_map[i] - v)
                tmp = helper(memo, sticker_maps, s)
                if tmp != -1:
                    ret = min(ret, 1+tmp)
            memo[target] = -1 if ret == float('inf') else ret
            return memo[target]
            

        sticker_maps = [[0] * 26 for _ in range(len(stickers))]
        for i, sticker in enumerate(stickers):
            for c in sticker:
                sticker_maps[i][ord(c)-ord('a')] += 1

        memo = {'': 0}
        return helper(memo, sticker_maps, target)
