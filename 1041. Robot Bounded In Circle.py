class Solution:
    def isRobotBounded(self, instructions: str) -> bool:




        def order(path, i, j, direction, logics):
            if command == 'G':
                i += logics[direction][0]
                j += logics[direction][1]
            elif command == 'R':
                direction = (direction+4+1)%4
            else:
                direction = ((direction+4-1)%4)
            return i, j, direction
        if instructions is None:
            return True

        logics = [(0,1), (1,0), (0,-1), (-1,0)]
        instructions *= 4
        i, j, direction= 0, 0, 0
        for command in instructions:
            i, j, direction = order(command, i, j, direction, logics)
        if i == 0 and j == 0:
            return True
        return False
