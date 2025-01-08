from collections import defaultdict, deque 

def setup_network():
    return defaultdict(list)

def connect_nodes(network, origin, destination):
    network[origin].append(destination)

def check_path_exists(network, beginning, target):
    nodes_seen = set()
    next_to_visit = deque([beginning])
    
    while len(next_to_visit) > 0:
        current = next_to_visit.popleft()
        if current == target:
            return True
        nodes_seen.add(current)
        
        for next_node in network[current]:
            if next_node not in nodes_seen and next_node not in next_to_visit:
                next_to_visit.append(next_node)
    return False

network = setup_network()
connection_pairs = [
    (1, 2), (2, 5), (3, 6), (4, 6), (6, 7), (4, 7)
]
for origin, dest in connection_pairs:
    connect_nodes(network, origin, dest)
    
start_point = int(input("Start node: "))
end_point = int(input("End node: "))

if check_path_exists(network, start_point, end_point):
    print("Existed")
else:
    print("Do not exist")


