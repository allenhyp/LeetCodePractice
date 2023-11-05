class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)
        wins, winner = 0, arr[0]
        for i in range(1, len(arr)):
            if winner > arr[i]:
                wins += 1
            else:
                winner = arr[i]
                wins = 1
            if wins == k:
                break
        return winner
