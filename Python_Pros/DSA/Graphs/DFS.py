def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(graph, neighbor, visited)

# Example Graph
graph = {1: [2, 3], 2: [4, 5], 3: [6, 7]}
dfs(graph, 1)
