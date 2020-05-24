#!/usr/bin/python

import networkx as nx
from networkx.algorithms import clique, bipartite

def planar(input_struct):

    G = nx.Graph()
    G.add_nodes_from(input_struct.get("nodes"))
    G.add_weighted_edges_from(input_struct.get("edges"))

    G_first_set = nx.Graph()
    G.add_nodes_from(input_struct.get("first_set_nodes"))
    G.add_weighted_edges_from(input_struct.get("first_set_edges"))
    choice = input_struct.get("choice")

    # check if graph is planar
    is_planar, _ = nx.check_planarity(G)

    # user choice
    if choice:
        if is_planar == True:
            # if choice is true and graph was planar
            display(Markdown("Corretto !"))
            #print("Corretto il grafo è planare, fornire un planar embedding")
        else:
            # if choice is true and graph was not planar
            display(Markdown("Soluzione errata"))
            #print("Soluzione errata")
    else:
        if is_planar == False:
        # if choice is flase and graph was not planar

            if G_first_set.number_of_nodes() == 6:

                # check k_33 graph with bipartition 
                bip_first_set = bipartite.is_bipartite(G_first_set)
                if bip_first_set:
                    display(Markdown("Controesempio corretto"))
                    #print("Controesempio corretto")
                else:
                    display(Markdown("Non è un K 3 3"))
                    #print("Non è un K 3 3")

            elif G_first_set.number_of_nodes() == 5:
                # check k 5 with clique

                clique = nx.find_cliques(G_first_set)
                sorted_list = sorted(clique, key=len) 

                if len(sorted_list[len(sorted_list)-1]) == 5:
                    display(Markdown("Controesempio corretto"))
                    #print("Controesempio corretto")
                else:
                    display(Markdown("Non è un K 5"))
                    #print("Non è un K 5")
            else:
                # wrong counterexample
                display(Markdown("Controesempio non valido"))
                #print("Controesempio non valido")
        else:
            # if choice is flase and graph was planar
            display(Markdown("Soluzione errata"))
            #print("Soluzione errata")