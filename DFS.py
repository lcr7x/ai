def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set if not provided
    visited.add(start)   # Mark the current node as visited
    print(start, end=" ")  # Print the visited node

    for neighbor in graph[start]:  # Explore neighbors recursively
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited  # Return the set of visited nodes

if __name__ == "__main__":
    # Define a graph using an adjacency list
    graph = {
        '1': ['2', '5'],
        '2': ['1', '3', '4'],
        '3': ['2'],
        '4': ['2'],
        '5': ['1', '6', '8'],
        '6': ['5', '7'],
        '7': ['6'],
        '8': ['5', '9'],
        '9': ['8', '10'],
        '10': ['9', '11'],
        '11': ['10']
    }
    # Example usage:
    print("Depth-First Traversal starting from node '1':")
    dfs(graph, '1')
