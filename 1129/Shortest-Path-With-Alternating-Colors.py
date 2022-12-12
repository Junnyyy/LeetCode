from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        neighbors = defaultdict(list)

        for source, neighbor in redEdges:
            neighbors[source].append((neighbor, 'red'))
        for source, neighbor in blueEdges:
            neighbors[source].append((neighbor, 'blue'))
        
        answer = [-1 for _ in range(n)]

        q = deque([(0, 'red', 0), (0, 'blue', 0)])
        visited = set()

        visited.add((0, 'red'))
        visited.add((0, 'blue'))
        answer[0] = 0

        while q:
            node, color, distance = q.popleft()         
            
            for neighbor, neighborColor in neighbors[node]:
                if (neighbor, neighborColor) in visited or color == neighborColor:
                    continue
                
                if answer[neighbor] < 0:
                    answer[neighbor] = distance + 1
                q.append((neighbor, neighborColor, distance + 1))
                visited.add((neighbor, neighborColor))

        return answer
        
