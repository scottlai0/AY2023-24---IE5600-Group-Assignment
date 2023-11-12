import sys
from graph import generateMap, Graph

def dijkstra(graph, start, end) -> list:
    
    # Shortest distance to reach all nodes which is updated per iteration
    shortest_dist = {}
    path = []
    # Keeps track of the paths that have led to specified nodes
    track_predecessor = {}
    
    unseen_nodes = graph.vertices.copy()
    
    # Infinite cost
    inf = sys.maxsize
    
    for node in unseen_nodes.keys():
        shortest_dist[node] = inf
    shortest_dist[start] = 0
    
    while unseen_nodes:
        min_dist_node = None
        
        for node in unseen_nodes.values():
            if not min_dist_node:
                min_dist_node = node.name
            # Update min_dist_node if another shortest path is found to the node FROM THE START NODE
            elif shortest_dist[node.name] < shortest_dist[min_dist_node]:
                min_dist_node = node.name
            

        for child in graph.vertices[min_dist_node].adjacentList:
            child_node = child['vertex'].name
            distance = child['distance']
            
            # Update min_dist if another shortest path is found to the currently-explored node FROM THE NEIGHBOUR NODES
            if distance + shortest_dist[min_dist_node] < shortest_dist[child_node]:
                shortest_dist[child_node] = distance + shortest_dist[min_dist_node]
                track_predecessor[child_node] = min_dist_node
        
        # Remove nodes that were iterated.
        unseen_nodes.pop(min_dist_node)
    
    current_node = end
    
    while current_node != start:
        path.insert(0, current_node)
        current_node = track_predecessor[current_node]
        
    path.insert(0, start)
    
    
    #if shortest_dist[end] != inf:  print(f"Shortest distance between {start} and {end} is {shortest_dist[end]}, optimal path: {path}")

    return path, shortest_dist[end]

def getShortestDistance(graph: Graph, vertices: list):
    curr_path = []
    total_dist = 0
    
    i = 0 
    vertex_list = vertices.copy()
    
    try:
        while i < len(vertex_list):
            # If the path already contains the current vertex, just move on since we assume it's delivered along the way
            if vertices[i] in curr_path:                
                i += 1
                continue
        
            if i == 0:
                prev_node = vertices[0]
                path, shortest_dist = dijkstra(graph, start = 'start_point', end = vertex_list[i])
            else:
                path, shortest_dist = dijkstra(graph, start = prev_node, end = vertex_list[i])
                path = path[1:]
                prev_node = vertices[i]
            
            curr_path += path
            total_dist += shortest_dist
            i += 1
        
        
        final_path, final_dist = dijkstra(graph, start = prev_node, end = 'start_point')
        curr_path += final_path[1:]
        total_dist += final_dist
        
        return curr_path, total_dist

    except KeyError:
        print("ERROR: One or more of the vertices are not reachable!")
        return []
    
if __name__ == "__main__":
    graph = generateMap()
    print()
    print('Generating Shortest Paths: ')

    delivery_path = ['R', 'R', 'H', 'S']
    shortest_path, shortest_distance = getShortestDistance(graph, vertices = delivery_path)
    print(' -> '.join([x + str('*') if x in delivery_path else x for x in shortest_path]))
    print('Total Distance:', shortest_distance)
    