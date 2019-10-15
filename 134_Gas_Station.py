class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, subsum, start = 0, float('inf'), 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < subsum:
                start = i + 1
                subsum = total
        return -1 if total < 0 else start % len(gas)
