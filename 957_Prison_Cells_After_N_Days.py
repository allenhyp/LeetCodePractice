class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        checked = {str(cells): N}
        while N:
            next_state = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            s = str(next_state)
            cells = next_state
            N -= 1
            if s in checked:
                N %= checked[s] - N
            checked[s] = N
        return cells
