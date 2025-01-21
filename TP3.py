def create_adjacency_matrix(graph):
    max_node = max(graph.keys())
    matrix = [[0] * (max_node + 1) for _ in range(max_node + 1)]
    
    for node in graph:
        for neighbor in graph[node]:
            matrix[node][neighbor] = 1
    
    print("Adjacency Matrix:")
    for i in range(1, max_node + 1):
        print(" ".join(map(str, matrix[i][1:])))

def inorder_traverse(current, graph, visited):
    if not current or visited[current]:
        return
        
    visited[current] = True
    neighbors = graph.get(current, [])
    
    if neighbors:
        inorder_traverse(neighbors[0], graph, visited)
    
    print(current, end=" ")
    
    for next_node in neighbors[1:]:
        inorder_traverse(next_node, graph, visited)

def main():
    graph = {
        1: [2, 3],
        2: [5, 6],
        3: [4],
        4: [8],
        5: [7],
        6: [],
        7: [],
        8: []
    }
    

    create_adjacency_matrix(graph)
    try:
        start_node = int(input("\nEnter node: "))
        visited = [False] * (max(graph.keys()) + 1)
        print("\nInorder Traversal:")
        inorder_traverse(start_node, graph, visited)
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()