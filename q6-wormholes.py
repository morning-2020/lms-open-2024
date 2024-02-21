import networkx as nx #Library im using for the stargraph

#All the code was originally done in a console window, so i just visually checked for two paths with a distance 1 apart since the list for sorted before printing

#Graph setup 

G = nx.Graph()

G.add_nodes_from([1,2,3,4,5,6,7,8,9])

G.add_edges_from([
    (1,2,{"weight": 65}),
    (2,3,{"weight": 35}),
    (1,4,{"weight": 38}),
    (2,5,{"weight": 47}),
    (3,6,{"weight": 54}),
    (4,5,{"weight": 52}),
    (5,6,{"weight": 39}),
    (4,7,{"weight": 46}),
    (5,8,{"weight": 51}),
    (6,9,{"weight": 57}),
    (7,8,{"weight": 43}),
    (8,9,{"weight": 63})
])

#Set up a list of all the possible paths in the graph
#Each path in the list is a tuple in the form of
#(start_node, end_node, [path_from_start_to_end_node], path_length)

dis = []  
for start in range(1, 9):
     for end in range(start+1, 10):
         dis += [(start,end,nx.dijkstra_path(G,start,end), nx.dijkstra_path_length(G,start,end))]

dis.sort(key=lambda x:x[3]) #Sorts the list by path length, lowest first

for i in dis:    #Prints every element of dis on a new line, in ascending order
    print(i)

dist = [x[3] for x in dis] #A list with just the path lengths

#Prints out the two nodes with the longest path between them

#Code to check if double the path length is possible in the graph, and if it is print both paths leghths

for i in dist:
    if i*2 in dist:
        print(i,i*2)

        
