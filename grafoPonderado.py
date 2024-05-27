import networkx as nx 
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.Graph()
        
    def add_edge(self, node1,node2, weight):
        self.graph.add_edge(node1,node2,weight=weight)
        
    
    
#Exemplo de uso
g = Graph()
g.add_edge('A','B', 5)
g.add_edge('B','C', 7)
g.add_edge('A','B', 3)

#Plotagem do grafo
pos = nx.spring_layout(g.graph) #Layout para organizar os nos
labels = nx.get_edge_attributes(g.graph, 'weight') #Obtem os pesos das arestas

nx.draw(g.graph, pos, with_labels=True, node_size=1000,node_color='skyblue', font_size=12,font_weight='bold')
nx.draw_networkx_edge_labels(g.graph, pos, edge_labels=labels)
plt.title('Grafo Ponderado')
plt.show()
