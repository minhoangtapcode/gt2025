class WeightedGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
        
    def add_edge(self, u, v, w):
        """Add an edge with weight to the graph"""
        u, v = u-1, v-1
        self.adj_matrix[u][v] = w
        self.adj_matrix[v][u] = w  # Since it's an undirected graph
        
    def print_weighted_matrix(self):
        print("Weighted Adjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(str(x) for x in row))
            
    def prim_mst(self, start_vertex):
        """Implementation of Prim's MST algorithm"""
        import heapq
        
        result = []
        visited = [False] * self.V
        pq = []  # Priority queue
        
        start_vertex -= 1  # Convert to 0-based indexing
        heapq.heappush(pq, (0, start_vertex, start_vertex))
        
        while pq:
            w, u, parent = heapq.heappop(pq)
            
            if visited[u]:
                continue
                
            visited[u] = True
            if u != parent:
                result.append([parent+1, u+1, w])  # Convert back to 1-based indexing
                
            for v in range(self.V):
                if self.adj_matrix[u][v] > 0 and not visited[v]:
                    heapq.heappush(pq, (self.adj_matrix[u][v], v, u))
                    
        return result
        
    def kruskal_mst(self):
        """Implementation of Kruskal's MST algorithm"""
        result = []
        edges = []
        
        for i in range(self.V):
            for j in range(i+1, self.V):
                if self.adj_matrix[i][j] > 0:
                    edges.append([i, j, self.adj_matrix[i][j]])
        
        edges.sort(key=lambda x: x[2])
        
        parent = list(range(self.V))
        
        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]
            
        def union(parent, x, y):
            parent[x] = y
            
        e = 0
        i = 0
        while e < self.V - 1 and i < len(edges):
            u, v, w = edges[i]
            i += 1
            x = find(parent, u)
            y = find(parent, v)
            
            if x != y:
                e += 1
                result.append([u+1, v+1, w])  # Convert back to 1-based indexing
                union(parent, x, y)
                
        return result

g = WeightedGraph(9)  # 9 vertices numbered from 1 to 9

edges = [
    (1, 2, 4), (1, 5, 1), (1, 7, 2),
    (2, 3, 7), (2, 6, 5),
    (3, 4, 1), (3, 6, 8),
    (4, 6, 6), (4, 8, 3), (4, 9, 4),
    (5, 6, 9), (5, 7, 10),
    (6, 9, 2),
    (7, 9, 8),
    (8, 9, 7)
]

for u, v, w in edges:
    g.add_edge(u, v, w)

g.print_weighted_matrix()

root = int(input("\nEnter the root node (1-9): "))

kruskal_mst = g.kruskal_mst()
prim_mst = g.prim_mst(root)

print("\nKruskal's MST edges:")
total_weight_kruskal = sum(w for _, _, w in kruskal_mst)
print("Edges:", kruskal_mst)
print("Total weight:", total_weight_kruskal)

print("\nPrim's MST edges (starting from vertex", root, "):")
total_weight_prim = sum(w for _, _, w in prim_mst)
print("Edges:", prim_mst)
print("Total weight:", total_weight_prim)