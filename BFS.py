from collections import deque

# BFS algorithm
def bfs(graph, root):
    visited = set()
    open = deque([root])
    visited.add(root)

    while open:
        vertex = open.popleft()
        print(str(vertex) + ",", end="")
        # Check if the vertex exists as a key in the graph before accessing its neighbors
        if vertex in graph:
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    open.append(neighbor)

if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 4, 4],  # Note: Duplicate '4' in the adjacency list
        2: [1, 5],
        3: [0, 6],
        4: [1, 6, 7],
        5: [2, 6, 8],
        6: [3],
        7: [6, 9],
        8: [9, 7],
        9: [] # Added node 9 with an empty list of neighbors to resolve KeyError
    }
    print("Following is Breadth-First Traversal:")
    bfs(graph, 0)
