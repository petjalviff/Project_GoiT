# def dfs_recursive(graph, vertex, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(vertex)
#     print(vertex, end=' ') # Відвідуємо вершину
#     print(visited)
#     for neighbor in graph[vertex]:
#         if neighbor not in visited:
#             dfs_recursive(graph, neighbor, visited)

# # Представлення графа за допомогою списку суміжності
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# # Виклик функції DFS
# dfs_recursive(graph, 'F')


# Встановлення бібліотеки NetworkX
# !pip install networkx matplotlib

# Імпортування необхідних модулів
import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вузлів (станцій метро)
stations = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
G.add_nodes_from(stations)
G.add_node("AB")
# Додавання ребер (ліній метро)
edges = [
    ("A", "B",), ("A", "C"),
    ("B", "D"), ("C", "D"),
    ("D", "E"), ("E", "F"), 
    ("F", "G"), ("G", "H"), 
    ("H", "I"), ("I", "A"), 
    ("C", "F"), ("B", "G"), 
    ("B", "I"), ("H", "B"), 
    ("AB","B")
]
G.add_edges_from(edges)
G.add_edge("AC", "C", weight=5)
G.add_edge("AC","G", weight=10)

print(G)
print(G.nodes())
print(G.edges())

DG=nx.DiGraph(G)
print(DG)

# Застосування алгоритму Дейкстри
shortest_paths = nx.single_source_dijkstra_path(G, source='A')
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='A')

print("найкоротші шляхи від вузла 'A' до всіх інших вузлів -",shortest_paths)  # виведе найкоротші шляхи від вузла 'A' до всіх інших вузлів
print("довжини найкоротших шляхів від вузла 'A' до всіх інших вузлів -",shortest_path_lengths)  # виведе довжини найкоротших шляхів від вузла 'A' до всіх інших вузлів

# Візуалізація графа
plt.figure(figsize=(8, 8))
# pos1 = nx.spring_layout(DG)  # Розташування вузлів
pos1 = nx.random_layout(DG)  # Розташування вузлів
nx.draw(DG, pos1, with_labels=True, node_color="skyblue", node_size=500, edge_color="green", font_size=8, font_weight="bold")
labels = nx.get_edge_attributes(DG, 'weight')
nx.draw_networkx_edge_labels(DG, pos1, edge_labels=labels)
plt.title("Транспортна мережа міста")
plt.show()

# plt.figure(figsize=(8, 8))
# pos2 = nx.spring_layout(G)  # Розташування вузлів
# nx.draw(G, pos2, with_labels=True, node_color="skyblue", node_size=500, edge_color="green", font_size=8, font_weight="bold")
# plt.title("Транспортна мережа міста")
# plt.show()

