from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph.get(node, []))

# Example Graph
graph = {1: [2, 3], 2: [4, 5], 3: [6, 7]}
bfs(graph, 1)
