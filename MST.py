from random import *

def edges_generator_v1(n):
    # takes in the number of vertexes and generator the weight of all edges
    # for n vertexes we will have 1+2+3+...+n-2+n-1 = n(n-1)/2 edges
    # for type 1 only
    edges = []

    for i in range(n - 1):
        for j in range(i, n):
            l = uniform(0,1)
            edge = [l, i, j]
            edges.append(edge)
    return edges

def edges_generator_v2(n):
    # points randomly pick from a unit square
    # for type 2 only
    xy_list = [[uniform(0,1), uniform(0,1)] for i in range(n)]
    edges = []

    for i in range(n-1):
        for j in range(1,n):
            first = xy_list[i]
            next = xy_list[j]
            distance = ((first[0] - next[0])**2 + (first[1] - next[1])**2)**(0.5)
            edge = [distance, i, j]
            edges.append(edge)
    return edges

def is_cycle(nodesT, edge):
    # determines if by adding the edge into edgesT (a 2D list) we will create a cycle
    # example of edgesT: [[1,2,3,4],[6,7]]
    mark1 = -1
    mark2 = -1
    for i in range(len(nodesT)):
        if edge[1] in nodesT[i]:
            mark1 = i
        if edge[2] in nodesT[i]:
            mark2 = i
        if mark1 is not -1 and mark2 is not -1:
            break
    if (mark1 == mark2) and (mark1 is not -1):     # a cycle
        return True
    elif (mark1 == mark2) and (mark1 is -1):    # a new edge
        nodesT.append([edge[1], edge[2]])
    elif mark1 is -1:
        nodesT[mark2].append(edge[1])
    elif mark2 is -1:
        nodesT[mark1].append(edge[2])
    else:                                      # combine two clusters
        nodesT[mark1] += nodesT[mark2].copy()
        del nodesT[mark2]
    return False

def minimum_spanning_tree(edges, num_nodes):
    # this function takes in a list of edges, number of nodes and returns the minimum weight of a MST. Kruskal's Algorithm.
    edges.sort()
    # print(edges)
    nodes_in_T = [[edges[0][1], edges[0][2]]]    # a 2D list of all the nodes in clusters. e.g. [[1,2,3,4],[6,7]]
    total_weight = edges[0][0]
    size_T = len(nodes_in_T[0])    # if a tree is formed, all nodes will be in 1 cluster. e.g. [[1,2,3,4,5,6,7]]

    for edge in edges[1:]:
        if size_T < num_nodes:
            if is_cycle(nodes_in_T, edge):
                # print(nodes_in_T)
                continue
            else:
                total_weight += edge[0]
                size_T = len(nodes_in_T[0])
                # print(nodes_in_T)
    # print(size_T)
    return total_weight


# now begin the stimulation
trials = [16, 32, 64, 128, 256]
for trial in trials:
    total_average_v1 = 0
    total_average_v2 = 0
    for i in range(100):
        edges_v1 = edges_generator_v1(trial)
        edges_v2 = edges_generator_v2(trial)
        mst_v1 = minimum_spanning_tree(edges_v1, trial)
        mst_v2 = minimum_spanning_tree(edges_v2, trial)
        total_average_v1 += mst_v1/trial
        total_average_v2 += mst_v2/trial
    average_v1 = total_average_v1/100
    average_v2 = total_average_v2/100
    s = "With n = " + str(trial) + ", \nthe average weight for type 1 is " + str(average_v1) + "\nthe average weight for type 2 is " + str(average_v2) + "\n"
    print(s)


