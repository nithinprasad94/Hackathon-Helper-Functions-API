# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.

def bfs(graph, start, goal):

    path = [] #holds path to return

    #Get connected nodes of the start node
    neighbour_nodes = graph.get_connected_nodes(start)

    agenda = [] #List of lists, each sub_list is a path to be explored ...
    
    agenda.append([start]) #initialize agenda with a single path of length 1, containing only
                           # the start node

    goal_found = False

    #Loop through and keep visiting new nodes until goal found
    while (goal_found == False):

        #Pop the front-most path from agenda
        temp_path = agenda.pop(0)

        terminal_node = temp_path[-1] #Node of interest is last node in the current path

        #If goal was found ... ie. path to goal removed from agenda!
        if terminal_node == goal:
            goal_found = True
            path = temp_path[:] 

        else:
            #Find neighbour nodes of terminal node
            neighbour_nodes = graph.get_connected_nodes(terminal_node)

            #Check each neighbour of terminal node
            for node in neighbour_nodes:
                #If node is not in path .... then feel free to add a new path to explore to the agenda
                if node not in temp_path:
                    new_path = temp_path[:] + [node]
                    agenda.append(new_path) #Append new path to end of agenda so it is explored in due time

    #Outside while loop ... means goal was found!
    return path
        
        
## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    path = [] #holds path to return

    #Get connected nodes of the start node
    neighbour_nodes = graph.get_connected_nodes(start)

    agenda = [] #List of lists, each sub_list is a path to be explored ...
    
    agenda.append([start]) #initialize agenda with a single path of length 1, containing only
                           # the start node

    goal_found = False

    #Loop through and keep visiting new nodes until goal found
    while (goal_found == False):

        #Pop the front-most path from agenda
        temp_path = agenda.pop(0)

        terminal_node = temp_path[-1] #Node of interest is last node in the current path

        #If goal was found ... ie. path to goal removed from agenda!
        if terminal_node == goal:
            goal_found = True
            path = temp_path[:] 

        else:
            #Find neighbour nodes of terminal node
            neighbour_nodes = graph.get_connected_nodes(terminal_node)

            #Check each neighbour of terminal node
            for node in neighbour_nodes:
                #If node is not in path .... then feel free to add a new path to explore to the agenda
                if node not in temp_path:
                    new_path = temp_path[:] + [node]
                    agenda.insert(0,new_path) #Append new path to start of agenda so it is explored first 

    #Outside while loop ... means goal was found!
    return path

## Now we're going to add some heuristics into the search.  
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    path = [] #holds path to return

    #Get connected nodes of the start node
    neighbour_nodes = graph.get_connected_nodes(start)

    agenda = [] #List of lists, each sub_list is a path to be explored ...
    
    agenda.append([start]) #initialize agenda with a single path of length 1, containing only
                           # the start node

    goal_found = False

    #Loop through and keep visiting new nodes until goal found
    while (goal_found == False):

        #Pop the front-most path from agenda
        temp_path = agenda.pop(0)

        terminal_node = temp_path[-1] #Node of interest is last node in the current path

        #If goal was found ... ie. path to goal removed from agenda!
        if terminal_node == goal:
            goal_found = True
            path = temp_path[:] 

        else:
            #Find neighbour nodes of terminal node
            heur_nodes = graph.get_connected_nodes(terminal_node) #unsorted

            #For each node found ... find its heuristic distance from goal ...
            heur_dists = []

            for heur_node in heur_nodes:
                heur_dist = graph.get_heuristic(heur_node,goal) 
                heur_dists.append(heur_dist) #unsorted

            neighbour_nodes = [] #Initialize empty neighbour nodes list
            neighbour_dists = [] #Only for testing purposes!!!

            #print "Original node list: " + str(heur_nodes)
            #print "Original heuristic list: " + str(heur_dists)
            #print "PRINTING HEURISTICS ..."
            #Do a loop to reorganize heur_nodes into neighbour_nodes by sorting by min heuristic
            while heur_nodes != []:
                min_dist = min(heur_dists)
                min_heur_index = heur_dists.index(min_dist)
                node_of_interest = heur_nodes[min_heur_index]
                #print "HEURISTIC FOR NODE " + node_of_interest + ": " + str(heur_dists[min_heur_index])
                heur_nodes.pop(min_heur_index)
                heur_dists.pop(min_heur_index)
                neighbour_nodes.insert(0,node_of_interest) #sorted such that lowest is last
                neighbour_dists.insert(0,min_dist) #testing only ...

                #Sorted this way since in the next loop, the nodes in the beginning
                # get added first to the path list, and thus we want the last path
                # added to be the heuristic best! (explored first)

            #print "Sorted node list: " + str(neighbour_nodes)
            #print "Sorted heuristic list: " + str(neighbour_dists)
            
            #Rest continues like DFS ...

            #Check each neighbour of terminal node
            for node in neighbour_nodes:
                #If node is not in path .... then feel free to add a new path to explore to the agenda
                if node not in temp_path:
                    new_path = temp_path[:] + [node]
                    agenda.insert(0,new_path) #Append new path to start of agenda so it is explored first 

    #Outside while loop ... means goal was found!
    return path

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the 
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    
    path = [] #holds path to return

    #Get connected nodes of the start node
    neighbour_nodes = graph.get_connected_nodes(start)

    agenda = [] #List of lists, each sub_list is a path to be explored ...
    
    agenda.append([start]) #initialize agenda with a single path of length 1, containing only
                           # the start node

    goal_found = False

    #print "==================================="
    #print "==================================="
    #print "Beam width: " + str(beam_width)
    
    #Loop through and keep exploring new paths until goal found or we run out of paths to explore
    while (goal_found == False) and (agenda != []):

        #print "Agenda at this level: " + str(agenda)
        
        agenda_fixed_paths = [] #Will store the n-best paths obtained by exploring
                                # n-best paths stored in agenda
        
        #Iterate through all paths of in agenda
        while agenda != [] and goal_found == False:        
        
            #Pop the front-most path from agenda
            temp_path = agenda.pop(0)

            terminal_node = temp_path[-1] #Node of interest is last node in the current path

            #If goal was found ... ie. path to goal removed from agenda!
            if terminal_node == goal:
                goal_found = True
                path = temp_path[:]
                #print "------------><-------------"
                #print "FOUND GOAL: " + str(path)

            else:
                #Find neighbour nodes of terminal node
                neighbour_nodes = graph.get_connected_nodes(terminal_node)

                #Check each neighbour of terminal node
                for node in neighbour_nodes:
                    #If node is not in path .... then feel free to add a new path to explore to the agenda
                    if node not in temp_path:
                        new_path = temp_path[:] + [node]
                        agenda_fixed_paths.append(new_path)

        #Now sort all the paths obtained in agenda_fixed_paths
        agenda_unsorted = agenda_fixed_paths[:]
        agenda_unsorted_heurs = []

        #print "Unsorted agenda for next level: " + str(agenda_unsorted)

        for temp_path in agenda_unsorted:
            terminal_node = temp_path[-1]
            agenda_unsorted_heurs.append(graph.get_heuristic(terminal_node,goal))

        agenda_sorted = []
        agenda_sorted_heurs = [] #Only for testing purposes ...

        #print "am i here?"
        while agenda_unsorted != [] and len(agenda_sorted) < beam_width:
            #Beam width comparison makes sure that the list is auto-pruned if necessary!

            #Get position of smallest heuristic in list
            min_heur = min(agenda_unsorted_heurs)
            min_pos = agenda_unsorted_heurs.index(min_heur)
            min_path = agenda_unsorted[min_pos]

            agenda_unsorted.pop(min_pos)
            agenda_unsorted_heurs.pop(min_pos)
            agenda_sorted.append(min_path)
            agenda_sorted_heurs.append(min_heur)
        #print "here i am"

        #print "Sorted agenda for next level: " + str(agenda_sorted)
        
        agenda = agenda_sorted[:] #Refresh agenda with path lengths increased by 1
                                  # capped if necessary!

    #Outside while loop ... means goal was found!
    return path

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):

    edges_list = []

    num_nodes = len(node_names)

    num_edges = num_nodes - 1 #Fences vs. Posts!

    path_length = 0

    if num_edges < 1:
        return 0 #Return path length of 0 
    
    for i in range(0,num_edges): 
        #i always refers to fence being examined - also corresponds to the left-post of
        # the said fence ....

        node1 = node_names[i]
        node2 = node_names[i+1]

        edge = graph.get_edge(node1, node2)

        edge_length = edge.length

        edges_list.append(edge)

        path_length += edge_length

    return path_length

##################################################################
#####Function(s) defined by me ...

#Given a path, the graph, and a path_list -> returns the index at
# which the path should be inserted (based on path lengths ONLY)!
def linear_search_for_bb(graph, paths_list, test_path):

    #print "entering linear search ..."
    if len(paths_list) == 0:
        index_to_insert = 0 #If path list has no elements, insert at 0!
        return index_to_insert
    #print "after default check for paths_list of length 0 ..."
    
    index_found = False
    curr_index = 0
    path_list_size = len(paths_list)
    test_path_length = path_length(graph, test_path)
    index_to_insert = 0
    
    #print str(paths_list)
    #print str(test_path)
    while (not index_found) and (curr_index < path_list_size):
        
        #print "Current index: " + str(curr_index)

        curr_path_length = path_length(graph, paths_list[curr_index])

        #print "Current path: " + str(paths_list[curr_index])
        #print "Current path length: " + str(curr_path_length)
        #print "Test path length: " + str(test_path_length)

        if test_path_length < curr_path_length:
            index_to_insert = curr_index
            index_found = True

        curr_index += 1

    if curr_index == path_list_size:
        index_to_insert = curr_index

    return index_to_insert

#Given a path, the graph, and a path_list -> returns the index at
# which the path should be inserted (based on path lengths + heuristic COMBINED)!
def linear_search_for_a_star(graph, goal, paths_list, test_path):

    #print "entering linear search ..."
    if len(paths_list) == 0:
        index_to_insert = 0 #If path list has no elements, insert at 0!
        return index_to_insert
    #print "after default check for paths_list of length 0 ..."
    
    index_found = False
    curr_index = 0
    path_list_size = len(paths_list)
    test_path_length = path_length(graph, test_path)
    test_path_term_node = test_path[-1]
    test_path_heuristic = graph.get_heuristic(test_path_term_node, goal)
    test_path_est_total = test_path_length + test_path_heuristic
    index_to_insert = 0
    
    #print str(paths_list)
    #print str(test_path)
    while (not index_found) and (curr_index < path_list_size):      

        curr_path = paths_list[curr_index]
        curr_path_length = path_length(graph, curr_path)
        curr_path_term_node = curr_path[-1]
        curr_path_heuristic = graph.get_heuristic(curr_path_term_node, goal)
        curr_path_est_total = curr_path_length + curr_path_heuristic

        #print "test total: " + str(test_path_est_total)
        #print "current total: " + str(curr_path_est_total)

        if test_path_est_total < curr_path_est_total:
            index_to_insert = curr_index
            index_found = True

        curr_index += 1

    if curr_index == path_list_size:
        index_to_insert = curr_index

    return index_to_insert

#Get the total path length for A*
def total_path_length(graph, goal, path):

    dist = path_length(graph,path)
    heur = graph.get_heuristic(path[-1],goal)
    total = dist + heur

    return total

#Test function for A* -> returns all the information about a list of paths!
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
    
##################################################################


def branch_and_bound(graph, start, goal):

    path = [] #holds path to return

    #Get connected nodes of the start node
    neighbour_nodes = graph.get_connected_nodes(start)

    agenda = [] #List of lists, each sub_list is a path to be explored ...
    
    agenda.append([start]) #initialize agenda with a single path of length 1, containing only
                           # the start node

    goal_found = False

    #Loop through and keep visiting new nodes until goal found
    while (goal_found == False):

        #print "======================="
        #print "Investigating new path ..."
        #print "Agenda: " + str(agenda)
        #Pop the front-most path from agenda
        temp_path = agenda.pop(0)
        #print "Current Path investigated ..." + str(temp_path)

        terminal_node = temp_path[-1] #Node of interest is last node in the current path

        #If goal was found ... ie. path to goal removed from agenda!
        if terminal_node == goal:
            goal_found = True
            path = temp_path[:] 

        else:
            #Find neighbour nodes of terminal node
            neighbour_nodes = graph.get_connected_nodes(terminal_node)

            
            #Check each neighbour of terminal node
            for node in neighbour_nodes:
                #If node is not in path .... then feel free to add a new path to explore to the agenda
                if node not in temp_path:
                    new_path = temp_path[:] + [node]
                    #print "Adding Path ... " + str(new_path)
                    #print "Length: " + str(path_length(graph,new_path))
                    #print "Current Agenda: " + str(agenda)
                    insert_index = linear_search_for_bb(graph, agenda, new_path)
                    #print "Index to insert @: " + str(insert_index)
                    agenda.insert(insert_index,new_path) #Append new path so as to preserve
                        # agenda ordering from low-path-length to high-path-length

    #Outside while loop ... means goal was found!
    return path

def a_star(graph, start, goal):
    #print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    #print "******************************************************************"
    #print "******************************************************************"
    #print "******************************************************************"
    #print "******************************************************************"   

    path = [] #holds path to return
    final_path_length = float('inf') #initial path length infinity - any path to goal is shorter than this!

    #Get connected nodes of the start node
    neighbour_nodes = graph.get_connected_nodes(start)

    agenda = [] #List of lists, each sub_list is a path to be explored ...

    extended_set = set([]) #Holds 'set' of nodes already explored!
    
    agenda.append([start]) #initialize agenda with a single path of length 1, containing only
                           # the start node

    #Loop through and keep visiting new nodes until goal found
    while (agenda != []):

        #print "======================="
        #print "SEEKING TO EXPLORE A PATH ..."
        #print "Investigating new path ..."
        #print "Agenda: " + str(agenda)
        #Pop the front-most path from agenda
        temp_path = agenda.pop(0)
        #print "Current Path: " + str(temp_path)

        terminal_node = temp_path[-1] #Node of interest is last node in the current path

        extended_set.add(terminal_node)

        #If goal was found ... ie. path to goal removed from agenda!
        if terminal_node == goal:

            temp_path_length = total_path_length(graph, goal, temp_path)
            if (temp_path_length) < (final_path_length):
                path = temp_path[:]
                final_path_length = temp_path_length
        #else:
        #Find neighbour nodes of terminal node
        neighbour_nodes = graph.get_connected_nodes(terminal_node)

        
        #Check each neighbour of terminal node
        for node in neighbour_nodes:
            #If node is not in path .... 
            if node not in temp_path:
                #If node is not in extended set already ...
                if node not in extended_set:
                
                    new_path = temp_path[:] + [node]
                    #print "New path valid to test ..." + str(new_path)

                    #Compute length of new path ...
                    new_path_length = total_path_length(graph, goal, new_path)

                    #If new path length doesn't exceed path length already in final_path_length ...
                    if (new_path_length < final_path_length):

                        #You may now feel free to add that path to the agenda!
                        
                        #(dist_list,heur_list,total_list) = path_info(graph, goal, agenda)
                        #print "<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>"
                        #print "SEEKING TO EXPLORE A NEW PATH!"
                        #print "Agenda right now: " + str(agenda)
                        #print "Distance list now: " + str(dist_list)
                        #print "Heuristic list now: " + str(heur_list)
                        #print "Total list now: " + str(total_list)
                        #print "Adding new path: " + str(new_path)
                        #print "New path properties ..."
                        new_path_dist = path_length(graph,new_path)
                        #print "Distance: " + str(new_path_dist)
                        new_path_heur = graph.get_heuristic(new_path[-1],goal)
                        #print "Heuristic: " + str(new_path_heur)
                        #print "Total: " + str(new_path_dist + new_path_heur)

                        #Note: don't add new path if it is already on extended list AND on

                        insert_index = linear_search_for_a_star(graph, goal, agenda, new_path)

                        agenda.insert(insert_index,new_path) #Append new path so as to preserve
                            # agenda ordering from low-path-length to high-path-length

    #Outside while loop ... means goal was found!
    return path

## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):

    edges_list = graph.edges
    nodes_set = set([])
    
    for edge in edges_list:
        nodes_set.add(edge.node1)
        nodes_set.add(edge.node2)

    nodes_list = list(nodes_set)

    graph_admissible = True
    
    while graph_admissible and nodes_list != []:

        node = nodes_list.pop() #pop last node off of the nodes list to examine

        optimal_path = branch_and_bound(graph,node,goal) #start <=> node
        node_dist = path_length(graph,optimal_path)
        node_heur = graph.get_heuristic(node,goal)

        #If heuristic is an overestimate ... graph is not admissible!
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

    #Want to loop the outer list until you reach the last node, which will have been touched
    # once by every node from the nodes_list_inner save for itself ....
    while graph_consistent and len(nodes_list_outer) > 1:

        node_outer = nodes_list_outer.pop()

        node_outer_heur = graph.get_heuristic(node_outer,goal)

        nodes_list_inner = nodes_list_outer[:]
        nodes_list_inner.pop()
        
        #Want to loop the inner list from one node popped with reference to the list so that
        # you don't ever compare a node with itself!
        while graph_consistent and len(nodes_list_inner) > 0:
            node_inner = nodes_list_inner.pop()
        
            node_inner_heur = graph.get_heuristic(node_inner,goal)

            #Check the condition!
            diff_heur_abs = abs(node_outer_heur - node_inner_heur)

            nodes_between_path = branch_and_bound(graph,node_outer,node_inner)
            dist_nodes = path_length(graph,nodes_between_path)

            if not (diff_heur_abs <= dist_nodes):
                graph_consistent = False

    return graph_consistent
            

HOW_MANY_HOURS_THIS_PSET_TOOK = '6 Hours'
WHAT_I_FOUND_INTERESTING = 'Branch & Bound, A*'
WHAT_I_FOUND_BORING = 'Not much - a little repetitive, but thats alright <3'
