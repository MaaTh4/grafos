# import networkx as nx
# import matplotlib.pyplot as plt

# #Cria um grafo não direcionado
# G = nx.Graph()

# #Adiciona nós ao grafo
# G.add_nodes_from([1, 2, 3, 4, 5])

# #Adiciona arestas ao grafo
# G.add_edges_from([(1, 2), (1,3), (2,3),(2,4),(3,5),(4,5)])

# #Visualiza o Grafo
# nx.draw(G, with_labels=True, node_color='lightblue', node_size=800, font_size=12, font_weight='bold')
# plt.title('Grafo com Nós e Arestas')
# plt.show()

import matplotlib.pyplot as plt
import networkx as nx

def plotar_arvore_geneologica():
    G = nx.DiGraph()
    
    #Adiciona Nós
    G.add_node("Você")
    G.add_node('Mãe')
    G.add_node('Pai')
    G.add_node('Avó materna')
    G.add_node('Avô materno')
    G.add_node('Avó paterna')
    G.add_node('Avô paterno')
    
    #Adicionando arestas
    G.add_edge('Avó materna', 'Mãe')
    G.add_edge('Avô materno', 'Mãe')
    G.add_edge('Avó paterna', 'Pai')
    G.add_edge('Avô paterno', "Pai")
    G.add_edge('Mãe', "Você")
    G.add_edge('Pai', 'Você')
    
    #Plotando
    pos = nx.spring_layout(G)
    nx.draw(G, pos,with_labels= True, node_size= 3000, node_color='skyblue', font_size=10, font_weight='bold')
    plt.show()
    
plotar_arvore_geneologica()
