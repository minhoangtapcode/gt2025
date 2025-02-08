import heapq

def initialize_network():
    """Create a weighted network with 13 nodes (A through M)."""
    network_size = 13
    network = [[0] * network_size for _ in range(network_size)]
    
    # Define connections with their weights
    connections = [
        ('A', 'B', 4), ('A', 'C', 1),
        ('B', 'F', 3),
        ('C', 'D', 8), ('C', 'F', 7),
        ('D', 'H', 5),
        ('E', 'H', 2), ('E', 'L', 2),
        ('F', 'E', 1), ('F', 'H', 1),
        ('G', 'L', 4), ('G', 'M', 4),
        ('H', 'G', 3), ('H', 'L', 6), ('H', 'M', 7),
        ('L', 'M', 4)
    ]
    
    # Convert node letters to array indices
    def get_node_index(node_letter):
        return ord(node_letter) - ord('A')
    
    # Populate network with connection weights
    for start, end, weight in connections:
        i, j = get_node_index(start), get_node_index(end)
        network[i][j] = network[j][i] = weight  # Undirected graph
        
    return network

def visualize_network(network):
    """Display the network's connection weights in a grid format."""
    print("\nNetwork Connection Weights:")
    for row in network:
        # Format each weight with consistent spacing
        print(" ".join(f"{weight:2}" for weight in row))

def find_optimal_route(network, origin, destination):
    """
    Find the shortest path between two nodes using Dijkstra's algorithm.
    Returns the path and total distance.
    """
    node_count = len(network)
    shortest_distances = [float('inf')] * node_count
    shortest_distances[origin] = 0
    route_tracking = [-1] * node_count
    processed_nodes = [False] * node_count
    
    # Priority queue to process nodes [(distance, node)]
    next_nodes = [(0, origin)]
    
    while next_nodes:
        # Get the node with smallest current distance
        distance_to_current, current = heapq.heappop(next_nodes)
        
        # Skip if node already processed
        if processed_nodes[current]:
            continue
            
        processed_nodes[current] = True
        
        # Check all neighboring nodes
        for next_node in range(node_count):
            weight = network[current][next_node]
            if weight > 0:  # If connection exists
                total_distance = distance_to_current + weight
                
                # Update if shorter path found
                if total_distance < shortest_distances[next_node]:
                    shortest_distances[next_node] = total_distance
                    route_tracking[next_node] = current
                    heapq.heappush(next_nodes, (total_distance, next_node))
    
    # Reconstruct the optimal path
    path = []
    current = destination
    while current != -1:
        path.append(current)
        current = route_tracking[current]
    path.reverse()
    
    return path, shortest_distances[destination]

def letter_to_index(letter):
    """Convert a node letter (A-M) to array index (0-12)."""
    return ord(letter.upper()) - ord('A')

def index_to_letter(index):
    """Convert an array index (0-12) to node letter (A-M)."""
    return chr(index + ord('A'))

def main():
    # Create and display the network
    network = initialize_network()
    visualize_network(network)
    
    try:
        # Get user input for start and end nodes
        start_node = input("\nStarting node (A-M): ").upper()
        end_node = input("Destination node (A-M): ").upper()
        
        # Convert letters to indices
        start_index = letter_to_index(start_node)
        end_index = letter_to_index(end_node)
        
        # Validate input
        if not (0 <= start_index < len(network) and 0 <= end_index < len(network)):
            raise ValueError("Node must be between A and M")
            
        # Find shortest path
        optimal_path, total_distance = find_optimal_route(network, start_index, end_index)
        
        # Convert indices back to letters for display
        path_letters = [index_to_letter(i) for i in optimal_path]
        
        # Display results
        print("\nOptimal Route Details:")
        print(f"Path: {' -> '.join(path_letters)}")
        print(f"Total Distance: {total_distance}")
        
    except ValueError as e:
        print(f"\nInput Error: {e}")
    except Exception as e:
        print(f"\nUnexpected Error: {e}")

if __name__ == "__main__":
    main()