from search import *

def bfs(graph, start, goal):

    path = [] 
    neighbour_nodes = graph.get_connected_nodes(start)

    agenda = [] 
    
    agenda.append([start])
    goal_found = False

    while (goal_found == False):
        temp_path = agenda.pop(0)

        terminal_node = temp_path[-1] 
        if terminal_node == goal:
            goal_found = True
            path = temp_path[:] 

        else:
            neighbour_nodes = graph.get_connected_nodes(terminal_node)

            for neighbour_node in neighbour_nodes:
                if neighbour_node in temp_path:
                    neighbour_nodes.pop(neighbour_nodes.index(neighbour_node))

            for node in neighbour_nodes:
                if node not in temp_path:
                    new_path = temp_path[:] + [node]
                    agenda.append(new_path)

    return path

def dfs(graph, start, goal):
    path = [] 

    neighbour_nodes = graph.get_connected_nodes(start)

    agenda = []    
    agenda.append([start])
    goal_found = False


    while (goal_found == False):
        temp_path = agenda.pop(0)

        terminal_node = temp_path[-1] 
        if terminal_node == goal:
            goal_found = True
            path = temp_path[:] 

        else:
            neighbour_nodes = graph.get_connected_nodes(terminal_node)

            for node in neighbour_nodes:
                if node not in temp_path:
                    new_path = temp_path[:] + [node]
                    agenda.insert(0,new_path) 
    return path

def hill_climbing(graph, start, goal):
    path = []
    
    neighbour_nodes = graph.get_connected_nodes(start)
    agenda = []
    agenda.append([start])
    goal_found = False

    while (goal_found == False):        
        temp_path = agenda.pop(0)

        terminal_node = temp_path[-1]
        
        if terminal_node == goal:
            goal_found = True
            path = temp_path[:] 

        else:
            heur_nodes = graph.get_connected_nodes(terminal_node) 

            heur_dists = []

            for heur_node in heur_nodes:
                heur_dist = graph.get_heuristic(heur_node,goal) 
                heur_dists.append(heur_dist)

            neighbour_nodes = [] 
            neighbour_dists = [] 


            while heur_nodes != []:
                min_dist = min(heur_dists)
                min_heur_index = heur_dists.index(min_dist)
                node_of_interest = heur_nodes[min_heur_index]
                heur_nodes.pop(min_heur_index)
                heur_dists.pop(min_heur_index)
                neighbour_nodes.insert(0,node_of_interest)
                neighbour_dists.insert(0,min_dist) 

            for node in neighbour_nodes:
                if node not in temp_path:
                    new_path = temp_path[:] + [node]
                    agenda.insert(0,new_path)
                    
    return path

def beam_search(graph, start, goal, beam_width):
    
    path = []
    neighbour_nodes = graph.get_connected_nodes(start)
    agenda = []
    
    agenda.append([start])
    
    goal_found = False

    while (goal_found == False) and (agenda != []):        
        agenda_fixed_paths = []
        
        while agenda != [] and goal_found == False:            
            temp_path = agenda.pop(0)
            terminal_node = temp_path[-1]
            
            if terminal_node == goal:
                goal_found = True
                path = temp_path[:]

            else:
                neighbour_nodes = graph.get_connected_nodes(terminal_node)
                for node in neighbour_nodes:
                    if node not in temp_path:
                        new_path = temp_path[:] + [node]
                        agenda_fixed_paths.append(new_path)

        agenda_unsorted = agenda_fixed_paths[:]
        agenda_unsorted_heurs = []

        for temp_path in agenda_unsorted:
            terminal_node = temp_path[-1]
            agenda_unsorted_heurs.append(graph.get_heuristic(terminal_node,goal))

        agenda_sorted = []
        agenda_sorted_heurs = []

        while agenda_unsorted != [] and len(agenda_sorted) < beam_width:
            min_heur = min(agenda_unsorted_heurs)
            min_pos = agenda_unsorted_heurs.index(min_heur)
            min_path = agenda_unsorted[min_pos]

            agenda_unsorted.pop(min_pos)
            agenda_unsorted_heurs.pop(min_pos)
            agenda_sorted.append(min_path)
            agenda_sorted_heurs.append(min_heur)

        agenda = agenda_sorted[:]
        
    return path

def path_length(graph, node_names):

    edges_list = []

    num_nodes = len(node_names)

    num_edges = num_nodes - 1

    path_length = 0

    if num_edges < 1:
        return 0  
    
    for i in range(0,num_edges): 

        node1 = node_names[i]
        node2 = node_names[i+1]

        edge = graph.get_edge(node1, node2)

        edge_length = edge.length

        edges_list.append(edge)

        path_length += edge_length

    return path_length

def linear_search_for_bb(graph, paths_list, test_path):

    if len(paths_list) == 0:
        index_to_insert = 0 
        return index_to_insert
    
    index_found = False
    curr_index = 0
    path_list_size = len(paths_list)
    test_path_length = path_length(graph, test_path)
    index_to_insert = 0
    
    while (not index_found) and (curr_index < path_list_size):

        curr_path_length = path_length(graph, paths_list[curr_index])

        if test_path_length < curr_path_length:
            index_to_insert = curr_index
            index_found = True

        curr_index += 1

    if curr_index == path_list_size:
        index_to_insert = curr_index

    return index_to_insert

def linear_search_for_a_star(graph, goal, paths_list, test_path):

    if len(paths_list) == 0:
        index_to_insert = 0 
        return index_to_insert
    
    index_found = False
    curr_index = 0
    path_list_size = len(paths_list)
    test_path_length = path_length(graph, test_path)
    test_path_term_node = test_path[-1]
    test_path_heuristic = graph.get_heuristic(test_path_term_node, goal)
    test_path_est_total = test_path_length + test_path_heuristic
    index_to_insert = 0

    while (not index_found) and (curr_index < path_list_size):      

        curr_path = paths_list[curr_index]
        curr_path_length = path_length(graph, curr_path)
        curr_path_term_node = curr_path[-1]
        curr_path_heuristic = graph.get_heuristic(curr_path_term_node, goal)
        curr_path_est_total = curr_path_length + curr_path_heuristic

        if test_path_est_total < curr_path_est_total:
            index_to_insert = curr_index
            index_found = True

        curr_index += 1

    if curr_index == path_list_size:
        index_to_insert = curr_index

    return index_to_insert

def total_path_length(graph, goal, path):

    dist = path_length(graph,path)
    heur = graph.get_heuristic(path[-1],goal)
    total = dist + heur

    return total

def path_info(graph, goal, path_list):

    dist_list = []
    heur_list = []
    total_list = []

    for path in path_list:
        dist = path_length(graph, path)
        dist_list.append(dist)
        term_node = path[-1]
        heur = graph.get_heuristic(term_node,goal)
        heur_list.append(heur)
        total = dist + heur
        total_list.append(total)

    return (dist_list,heur_list,total_list)

def branch_and_bound(graph, start, goal):

    path = []
    neighbour_nodes = graph.get_connected_nodes(start)
    agenda = []    
    agenda.append([start])
    goal_found = False

    while (goal_found == False):
        temp_path = agenda.pop(0)
        terminal_node = temp_path[-1]
        
        if terminal_node == goal:
            goal_found = True
            path = temp_path[:] 

        else:
            neighbour_nodes = graph.get_connected_nodes(terminal_node)

            for node in neighbour_nodes:
                if node not in temp_path:
                    new_path = temp_path[:] + [node]
                    insert_index = linear_search_for_bb(graph, agenda, new_path)
                    agenda.insert(insert_index,new_path)
    return path

def a_star(graph, start, goal):
    path = []
    final_path_length = float('inf')
    
    neighbour_nodes = graph.get_connected_nodes(start)
    agenda = []    
    extended_set = set([])    
    agenda.append([start])
    
    while (agenda != []):
        temp_path = agenda.pop(0)
        terminal_node = temp_path[-1]
        extended_set.add(terminal_node)

        if terminal_node == goal:
            temp_path_length = total_path_length(graph, goal, temp_path)
            if (temp_path_length) < (final_path_length):
                path = temp_path[:]
                final_path_length = temp_path_length
        neighbour_nodes = graph.get_connected_nodes(terminal_node)

        for node in neighbour_nodes:
            if node not in temp_path:
                if node not in extended_set:                
                    new_path = temp_path[:] + [node]

                    new_path_length = total_path_length(graph, goal, new_path)

                    if (new_path_length < final_path_length):                        
                        new_path_dist = path_length(graph,new_path)
                        new_path_heur = graph.get_heuristic(new_path[-1],goal)
                        insert_index = linear_search_for_a_star(graph, goal, agenda, new_path)

                        agenda.insert(insert_index,new_path)
                        
    return path

def is_admissible(graph, goal):

    edges_list = graph.edges
    nodes_set = set([])
    
    for edge in edges_list:
        nodes_set.add(edge.node1)
        nodes_set.add(edge.node2)

    nodes_list = list(nodes_set)

    graph_admissible = True
    
    while graph_admissible and nodes_list != []:

        node = nodes_list.pop()
        
        optimal_path = branch_and_bound(graph,node,goal)
        node_dist = path_length(graph,optimal_path)
        node_heur = graph.get_heuristic(node,goal)

        if node_dist < node_heur: 
            graph_admissible = False

    return graph_admissible
            
def is_consistent(graph, goal):

    edges_list = graph.edges
    nodes_set = set([])
    
    for edge in edges_list:
        nodes_set.add(edge.node1)
        nodes_set.add(edge.node2)

    nodes_list_outer = list(nodes_set)
    nodes_list_inner = list(nodes_set)

    graph_consistent = True

    while graph_consistent and len(nodes_list_outer) > 1:

        node_outer = nodes_list_outer.pop()

        node_outer_heur = graph.get_heuristic(node_outer,goal)

        nodes_list_inner = nodes_list_outer[:]
        nodes_list_inner.pop()
        
        while graph_consistent and len(nodes_list_inner) > 0:
            node_inner = nodes_list_inner.pop()        
            node_inner_heur = graph.get_heuristic(node_inner,goal)
            diff_heur_abs = abs(node_outer_heur - node_inner_heur)

            nodes_between_path = branch_and_bound(graph,node_outer,node_inner)
            dist_nodes = path_length(graph,nodes_between_path)

            if not (diff_heur_abs <= dist_nodes):
                graph_consistent = False

    return graph_consistent

GRAPH3 = Graph(edgesdict=[ 
        {NAME: 'e1', VAL: 6, NODE1:'S', NODE2:'B' },
        {NAME: 'e2', VAL:10, NODE1:'S', NODE2:'A' },
        {NAME: 'e3', VAL:10, NODE1:'A', NODE2:'B' },
        {NAME: 'e4', VAL: 7, NODE1:'B', NODE2:'C' },
        {NAME: 'e5', VAL: 4, NODE1:'A', NODE2:'D' },
        {NAME: 'e6', VAL: 2, NODE1:'C', NODE2:'D' },
        {NAME: 'e7', VAL: 6, NODE1:'C', NODE2:'G' },
        {NAME: 'e8', VAL: 8, NODE1:'G', NODE2:'D' } ],
               heuristic={'G':{"S":0,"A":2,"B":5,"C":6,"D":5}})

print("BFS: " + str(bfs(GRAPH3,'S','G')))
print("DFS: " + str(dfs(GRAPH3,'S','G')))
print("HILL CLIMBING: " + str(hill_climbing(GRAPH3,'S','G')))
print("BEAM SEARCH: " + str(beam_search(GRAPH3,'S','G',3)))
print("BRANCH AND BOUND: " + str(branch_and_bound(GRAPH3,'S','G')))
print("A*: " + str(a_star(GRAPH3,'S','G')))
print("Is the graph ADMISSIBLE? " + str(is_admissible(GRAPH3,'G')))
print("Is the graph CONSISTENT? " + str(is_consistent(GRAPH3,'G')))






