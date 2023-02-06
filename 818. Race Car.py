class Solution:
    def racecar(self, target: int) -> int:



        q = deque([(0, 1)])
        visited = set()
        visited.add((0,  1))
        moves  = 0
        while q:
            n = len(q)
            for _ in range(n):
                position, speed = q.popleft()
                if position == target:
                    return moves
                if (position+speed, speed*2) not in visited:
                    visited.add((position+speed, speed*2))
                    q.append((position+speed, speed*2))
                
                if (position+speed > target and speed >0) or (position+speed < target and speed < 0):
                    speed = -1 if speed > 0 else 1
                    if (position, speed) not in visited:
                        visited.add((position,  speed))
                        q.append((position,  speed))
            moves += 1
        
        return -1
