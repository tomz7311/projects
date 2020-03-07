import networkx as nx
import pylab


def travel(graph, new_graph, adjacent, cities, starting_city):
    #start at start node
    #check to see which edge is lowest at node
    #pick that edge and go to next node
    #repeat
    #need to get back to start node


    total = 0
    edge = 0
    dist = 100
    destination = 0
    visited = [0 for x in range(graph.number_of_nodes())]

    print('Starting city', starting_city)
    for i in range(len(adjacent[0])):
        if graph.has_edge(starting_city, i):
            edge = adjacent[starting_city][i]
        if dist > edge and edge is not 0:
            dist = edge
            destination = i

    total = dist + total
    adjacent[destination][starting_city] = float('inf')
    new_graph.add_weighted_edges_from([(starting_city, destination, dist)], weight='distance')
    next_city = destination
    # put visited cities in an array and check if city has already been visited
    visited[destination] = destination
    count = 2
    print("Distance from", starting_city, "to", next_city, "is", dist, ". Total distance is", total)

    while next_city is not starting_city:
        edge = 0
        dist = 100
        possible_city = destination
        for c in range(len(adjacent)):
            #checks if there is an edge connected city and has not already been visited
            if graph.has_edge(possible_city, c) and c != visited[c]:
                edge = adjacent[possible_city][c]
            if dist > edge and edge is not 0:
                dist = edge
                destination = c
        #if all connected cities to current city have been visited stop
        if next_city is destination:
            print("Cities connected to", next_city, "have all be visited. Cannot finish travel.")
            break
        total = dist + total
        new_graph.add_weighted_edges_from([(next_city, destination, dist)], weight='distance')
        print("Distance from", next_city, "to", destination,  "is",  dist, ". Total distance is", total)
        next_city = destination
        # put visited cities in an array and check if city has already been visited
        #visited[destination] = cities[destination]
        count = count + 1


    return new_graph

#creates adjacency matrix
def conversion_to_adjacency(graph, city):
    c = graph.number_of_nodes()
    r = graph.number_of_nodes()
    mat = [[0 for x in range(c)] for x in range(r)]

    for i in range(r):
        for j in range(c):
            if graph.has_edge(i, j):
                mat[i][j] = sum(G.get_edge_data(i, j).values())
            else:
                mat[i][j] = float('inf')
    return mat

if __name__ == '__main__':
    G = nx.Graph()
    pos = nx.spring_layout(G)
    mylist = ['Atlanta', 'Decatur', 'Marietta', 'Canton', 'Cumming', 'Kennesaw', 'Cartersville', 'Rome',
                'Duluth', 'Buckhead', 'Sugar Hill', 'Woodstock', 'Smyrna', 'Norcross', 'Sandy Springs', 'Doraville']

    G.add_nodes_from(mylist)
    #edges of connected cities
    G.add_weighted_edges_from([
        (0, 2, 25),
        (0, 15, 20),
        (9, 15, 19),
        (4, 2, 38),
        (0, 9, 8),
        (3, 2, 23),
        (11, 14, 26),
        (9, 13, 22),
        (9, 12, 11),
        (12, 2, 7),
        (8, 10, 10),
        (8, 4, 19),
        (11, 6, 26),
        (7, 6, 26),
        (14, 5, 24),
        (8, 15, 12),
        (7, 8, 80),
        (4, 5, 40),
        (10, 8, 33),
        (11, 3, 12),
        (13, 4, 27),
        (3, 12, 31),
        (10, 4, 11),
        (8, 0, 8),
        (6, 5, 20),
        (3, 5, 21),
        (15, 13, 5),
        (11, 2, 11),
        (10, 14, 32),
        (14, 8, 19),
        (5, 7, 44),
        (7, 6, 26),
        (7, 14, 65)]
        , weight='distance')

    labels ={}
    for i in range(len(mylist)):
        labels[i] = '$',mylist[i],'$'

    G2 = nx.Graph()

    city_adjacency = conversion_to_adjacency(G, mylist)

    #adjacency matrix
    for i in range(len(city_adjacency)):
        print(city_adjacency[i])

    edge_labels = dict([((u, v,), d['distance'])
                        for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    G2 = travel(G, G2, city_adjacency, mylist, 1)

    pylab.figure(1)
    nx.draw(G, with_labels=True)




    pylab.show()

    pylab.figure(2)
    nx.draw(G2, with_labels=True)
    pylab.show()
