class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        b = '|'.join(board)
        x, o = (any(p * 3 in b[s::d] for s in range(9) for d in [1, 3, 4, 5]) for p in 'XO')
        m = b.count('X') - b.count('O')
        return (m == 0 and not x) or (m == 1 and not o)


class Solution:
    def check(self, state):
        if state[0] == state[1] and state[1] == state[2]:
            if state[0] == 'X':
                return 1.
            elif state[0] == 'O':
                return 0.9
        return 0.

    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        state = []
        x_num = 0
        o_num = 0
        w_num = 0.
        for b in board:
            state.append(list(b));
        for s in state:
            for ss in s:
                if ss == 'X':
                    x_num += 1
                elif ss == 'O':
                    o_num += 1
        if x_num == 0 and o_num > 0:
            return False
        elif not (x_num - o_num == 1 or x_num == o_num):
            return False
        else:
            column = [[],[],[]]
            for s in state:
                w_num += self.check(s)
                column[0].append(s[0])
                column[1].append(s[1])
                column[2].append(s[2])
            for c in column:
                w_num += self.check(c)
            w_num += self.check([state[0][0], state[1][1], state[2][2]])
            w_num += self.check([state[0][2], state[1][1], state[2][0]])
            if w_num > 1.:
                return False
            elif w_num == 1.:
                if o_num >= x_num:
                    return False
            elif w_num == 0.9:
                if o_num != x_num:
                    return False
        return True
