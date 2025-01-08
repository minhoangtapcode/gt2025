from collections import defaultdict, deque

class GraphStructure:
    @staticmethod
    def create_matrix(connections, size):
        result = [[0] * size for _ in range(size)]
        for start, end in connections:
            result[start - 1][end - 1] = 1
        return result

    @staticmethod
    def show_matrix(matrix):
        print("Adjacency Matrix:")
        for row in matrix:
            print(" ".join(map(str, row)))

    @staticmethod
    def get_adjacency(matrix):
        result = defaultdict(list)
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == 1:
                    result[i + 1].append(j + 1)
        return result

class ComponentAnalyzer:
    @staticmethod
    def analyze_weak(matrix):
        def get_undirected(adj_list):
            result = defaultdict(list)
            for node in adj_list:
                for neighbor in adj_list[node]:
                    result[node].append(neighbor)
                    result[neighbor].append(node)
            return result
            
        def process_component(start_node, graph, visited):
            to_process = deque([start_node])
            while to_process:
                current = to_process.popleft()
                for next_node in graph[current]:
                    if next_node not in visited:
                        visited.add(next_node)
                        to_process.append(next_node)
        
        adjacency = GraphStructure.get_adjacency(matrix)
        undirected = get_undirected(adjacency)
        visited = set()
        count = 0
        
        for node in range(1, len(matrix) + 1):
            if node not in visited:
                count += 1
                visited.add(node)
                process_component(node, undirected, visited)
        
        return count

    @staticmethod
    def analyze_strong(matrix):
        def process_forward(node, adj_list, seen, ordering):
            seen.add(node)
            for next_node in adj_list[node]:
                if next_node not in seen:
                    process_forward(next_node, adj_list, seen, ordering)
            ordering.append(node)
            
        def process_backward(node, rev_list, seen):
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in seen:
                    seen.add(current)
                    stack.extend(rev_list[current])
        
        adjacency = GraphStructure.get_adjacency(matrix)
        visited = set()
        finish_order = []
        
        for node in range(1, len(matrix) + 1):
            if node not in visited:
                process_forward(node, adjacency, visited, finish_order)
        
        reversed_adj = defaultdict(list)
        for node, neighbors in adjacency.items():
            for neighbor in neighbors:
                reversed_adj[neighbor].append(node)
        
        visited.clear()
        count = 0
        
        while finish_order:
            node = finish_order.pop()
            if node not in visited:
                count += 1
                process_backward(node, reversed_adj, visited)
        
        return count


edges = [
    (1, 2), (1, 4), (2, 3), (2, 6),
    (6, 3), (6, 4), (5, 4), (7, 6),
    (7, 3), (7, 5), (7, 8), (8, 9), (5, 9)
]
nodes = 9

matrix = GraphStructure.create_matrix(edges, nodes)
GraphStructure.show_matrix(matrix)

weak = ComponentAnalyzer.analyze_weak(matrix)
strong = ComponentAnalyzer.analyze_strong(matrix)

print(f"\nNumber of weakly connected components: {weak}")
print(f"Number of strongly connected components: {strong}")
 