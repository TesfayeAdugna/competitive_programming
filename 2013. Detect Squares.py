class DetectSquares:

    def __init__(self):
        
        self.square_dict = collections.defaultdict(int)
        self.x_dict = collections.defaultdict(set)
        

    def add(self, point: List[int]) -> None:
        
        pointSet = tuple(point)
        self.square_dict[pointSet] += 1
        self.x_dict[point[0]].add(point[1])
        
    def count(self, point: List[int]) -> int:
        
        if point[0] not in self.x_dict:
            return 0
        
        count = 0
        
        for neigh in self.x_dict[point[0]]:
            distance = abs(neigh - point[1])
            
            if distance != 0:
            
                if (point[0] - distance, neigh) in self.square_dict and (point[0] - distance, point[1]) in self.square_dict:
                    count += (self.square_dict[(point[0] - distance, neigh)] * self.square_dict[(point[0] - distance, point[1])] 
                            * self.square_dict[(point[0], neigh)])

                if (point[0] + distance, neigh) in self.square_dict and (point[0] + distance, point[1]) in self.square_dict:
                    count += (self.square_dict[(point[0] + distance, neigh)] * self.square_dict[(point[0] + distance, point[1])] 
                            * self.square_dict[(point[0], neigh)])
                
        return count

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
