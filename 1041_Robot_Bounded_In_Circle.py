class Solution:        
    def move(self, i, j, d, instruction):
            if instruction == 'G':
                i, j = i + self.direction[d][0], j + self.direction[d][1]
            elif instruction == 'L':
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
            return i, j, d
    
    def isRobotBounded(self, instructions: str) -> bool:
        self.direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        x, y, yaw = 0, 0, 0
        for ins in instructions:
            x, y, yaw = self.move(x, y, yaw, ins)
        if (x, y) == (0, 0) or yaw != 0:
            return True
        else:
            return False
