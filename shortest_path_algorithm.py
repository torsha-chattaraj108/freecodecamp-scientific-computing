my_graph={'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]}
def shortest_path(graph,start,target=''):
    unvisited=list(graph)

    distances={node:0 if node==start else float('inf') for node in graph}#This assigns 0 to starting node and all other nodes to infinity

    paths={node:[] for node in graph}#Creates a dictionary to store the list of steps for each path

    while unvisited:#Loops until all nodes are visited

        current=min(unvisited,key=distances.get)#Finds unvisited node with the shortest known distance
        for node,distance in graph[current]:#Checks every node connected to the spot and their distance from it
            if distance+distances[current]<distances[node]:#Checks if the distance of the neighbour node from the current spot is shorter than the assigned one
                distances[node]=distance+distances[current]#If it is then it assigns the new distance for the neighbouring node
                if paths[node] and paths[current][-1]==node:#Safely clones the path if it already loops back to this neighbour
                    paths[node]=paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)#Marks the current node as visited 
    targets_to_print=[target] if target else graph#Checks if only a specific target is asked else prints the whole
    for node in targets_to_print:
            if node==start:
                continue
            print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    return distances,paths
shortest_path(my_graph,'A')
