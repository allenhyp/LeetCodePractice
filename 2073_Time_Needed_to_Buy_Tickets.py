class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0
        for i in range(len(tickets)):
            if i <= k:
                # tickets[i] contributes min(tickets[i], tickets[k])
                total += min(tickets[i], tickets[k])
            else:
                # tickts[i] contriburtes min(tickets[k]-1, tickets[i])
                total += min(tickets[k]-1, tickets[i])
        return total
