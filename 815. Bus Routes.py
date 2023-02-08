class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        

        graph = defaultdict(set)
        for index, route in enumerate(routes):
            for stop in route:
                graph[stop].add(index)

        # print(graph)
        queue = deque([source])
        level = 0
        visited = set()
        visited_route = set()
        visited.add(source)
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == target: return level
                for route_index in graph[curr]:
                    if route_index not in visited_route:
                        for route in routes[route_index]:
                            if route not in visited:
                                visited.add(route)
                                queue.append(route)
                        visited_route.add(route_index)
            level += 1
            
        return -1
