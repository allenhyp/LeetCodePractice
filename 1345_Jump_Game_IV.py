class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        nei = collections.defaultdict(list)
        for i, v in enumerate(arr):
            nei[v].append(i)
        queue, visited_num, visited_pos = collections.deque([(0, 0)]), set(), set()
        while queue:
            pos, step = queue.pop()
            if pos == n - 1: return step
            num = arr[pos]
            visited_pos.add(pos)
            for nxt in [pos - 1, pos + 1] + nei[num] * (num not in visited_num):
                if nxt not in visited_pos and 0 <= nxt < n:
                    queue.appendleft((nxt, step + 1))
            visited_num.add(num)
        return 0
