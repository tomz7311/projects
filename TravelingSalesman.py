import networkx as nx
import matplotlib.pyplot as plt


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
        if graph.has_edge(cities[cities.index(starting_city)], cities[i]):
            edge = adjacent[cities.index(starting_city)][i]
        if dist > edge and edge is not 0:
            dist = edge
            destination = i

    total = dist + total
    adjacent[destination][cities.index(starting_city)] = float('inf')
    new_graph.add_weighted_edges_from([(cities[cities.index(starting_city)], cities[destination], dist)], weight='distance')
    next_city = cities[destination]
    # put visited cities in an array and check if city has already been visited
    visited[destination] = cities[destination]
    count = 2
    print("Distance from", starting_city, "to", next_city, "is", dist, ". Total distance is", total)

    while next_city is not starting_city:
        edge = 0
        dist = 100
        possible_city = destination
        for c in range(len(adjacent)):
            #checks if there is an edge connected city and has not already been visited
            if graph.has_edge(cities[possible_city], cities[c]) and cities[c] != visited[c]:
                edge = adjacent[possible_city][c]
            if dist > edge and edge is not 0:
                dist = edge
                destination = c
        #if all connected cities to current city have been visited stop
        if next_city is cities[destination]:
            print("Cities connected to", next_city, "have all be visited. Cannot finish travel.")
            break
        total = dist + total
        new_graph.add_weighted_edges_from([(cities[cities.index(next_city)], cities[destination], dist)], weight='distance')
        print("Distance from", next_city, "to", cities[destination],  "is",  dist, ". Total distance is", total)
        next_city = cities[destination]
        # put visited cities in an array and check if city has already been visited
        visited[destination] = cities[destination]
        count = count + 1


    return new_graph

#creates adjacency matrix
def conversion_to_adjacency(graph, city):
    c = graph.number_of_nodes()
    r = graph.number_of_nodes()
    mat = [[0 for x in range(c)] for x in range(r)]

    for i in range(r):
        for j in range(c):
            if graph.has_edge(city[i], city[j]):
                mat[i][j] = sum(G.get_edge_data(city[i], city[j]).values())
            else:
                mat[i][j] = float('inf')
    return mat

if __name__ == '__main__':
    G = nx.Graph()
    mylist = ['Atlanta', 'Decatur', 'Marietta', 'Canton', 'Cumming', 'Kennesaw', 'Cartersville', 'Rome',
                'Duluth', 'Buckhead', 'Sugar Hill', 'Woodstock', 'Smyrna', 'Norcross', 'Sandy Springs', 'Doraville']

    G.add_nodes_from(mylist)
    #edges of connected cities
    G.add_weighted_edges_from([
        ('Atlanta', 'Marietta', 25),
        ('Atlanta', 'Doraville', 20),
        ('Buckhead', 'Doraville', 19),
        ('Cumming', 'Marietta', 38),
        ('Atlanta', 'Buckhead', 8),
        ('Canton', 'Marietta', 23),
        ('Woodstock', 'Sandy Springs', 26),
        ('Buckhead', 'Norcross', 22),
        ('Buckhead', 'Smyrna', 11),
        ('Smyrna', 'Marietta', 7),
        ('Duluth', 'Sugar Hill', 10),
        ('Duluth', 'Cumming', 19),
        ('Woodstock', 'Cartersville', 26),
        ('Rome', 'Cartersville', 26),
        ('Sandy Springs', 'Kennesaw', 24),
        ('Decatur', 'Doraville', 12),
        ('Rome', 'Duluth', 80),
        ('Cumming', 'Kennesaw', 40),
        ('Sugar Hill', 'Decatur', 33),
        ('Woodstock', 'Canton', 12),
        ('Norcross', 'Cumming', 27),
        ('Canton', 'Smyrna', 31),
        ('Sugar Hill', 'Cumming', 11),
        ('Decatur', 'Atlanta', 8),
        ('Cartersville', 'Kennesaw', 20),
        ('Canton', 'Kennesaw', 21),
        ('Doraville', 'Norcross', 5),
        ('Woodstock', 'Marietta', 11),
        ('Sugar Hill', 'Sandy Springs', 32),
        ('Sandy Springs', 'Duluth', 19),
        ('Kennesaw', 'Rome', 44),
        ('Rome', 'Cartersville', 26),
        ('Rome', 'Sandy Springs', 65)]
        , weight='distance')

    G2 = nx.Graph()

    city_adjacency = conversion_to_adjacency(G, mylist)

    #adjacency matrix
    for i in range(len(city_adjacency)):
        print(city_adjacency[i])

    G2 = travel(G, G2, city_adjacency, mylist, 'Rome')
    plt.figure()
    nx.draw(G, with_labels=True)
    plt.show()

    plt.figure()
    nx.draw(G2, with_labels=True)
    plt.show()



