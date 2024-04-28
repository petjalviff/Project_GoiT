# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None
# #         self.prev = None
    
# #     def __str__(self):
# #         return str(self.data)


# # class DoublyLinkedList:
# #     def __init__(self):
# #         self.head = None
# #         self.tail = None

# #     # Додавання вузла на кінець списку
# #     def append(self, data):
# #         new_node = Node(data)
# #         if self.head is None:
# #             self.head = new_node
# #             self.tail = self.head
# #         else:
# #             self.tail.next = new_node
# #             new_node.prev = self.tail
# #             self.tail = new_node

# #     # Додавання вузла на початок списку
# #     def push(self, data):
# #         new_node = Node(data)
# #         new_node.next = self.head
# #         if self.head:
# #             self.head.prev = new_node
# #         else:
# #             self.tail = new_node
# #             self.head = new_node

# #     # Додавання вузла після заданого вузла
# #     def insert_after(self, prev_node, data):
# #         if not prev_node:
# #             return
# #         new_node = Node(data)
# #         new_node.next = prev_node.next
# #         prev_node.next = new_node
# #         new_node.prev = prev_node
# #         if new_node.next:
# #             new_node.next.prev = new_node
# #         else:
# #             self.tail = new_node

# #     # Додавання вузла перед заданим вузлом
# #     def insert_before(self, next_node, data):
# #         if not next_node:
# #             return
# #         new_node = Node(data)
# #         new_node.prev = next_node.prev
# #         next_node.prev = new_node
# #         new_node.next = next_node
# #         if new_node.prev:
# #             new_node.prev.next = new_node
# #         else:
# #             self.head = new_node

# #     def remove(self, data):
# #         current_node = self.head
# #         while current_node:
# #             if current_node.data == data:
# #                 if current_node.prev:
# #                     current_node.prev.next = current_node.next
# #                 else:
# #                     self.head = current_node.next
# #                 if current_node.next:
# #                     current_node.next.prev = current_node.prev
# #                 else:
# #                     self.tail = current_node.prev
# #                 current_node.prev = None
# #                 current_node.next = None
# #             return True
# #         current_node = current_node.next
# #         return False

# #     def search(self, target_data):
# #         current_node = self.head
# #         while current_node:
# #             if current_node.data == target_data:
# #                 return current_node
# #             current_node = current_node.next
# #         return None

# # ddl=DoublyLinkedList()

# # ddl.append(1)
# # ddl.append("Andrii")

# # nnd=Node

# # print(nnd)


# # *************************************Hash Tags

# # my_dict = {}
# # my_dict["key1"] = "value1"
# # my_dict["key2"] = "value2"
# # print(my_dict)  # {'key1': 'value1', 'key2': 'value2'}

# # del my_dict["key1"]

# # print(my_dict)

# # my_dict["hash"]="Andrii"

# # print(my_dict)
# # v=my_dict.get("key2")
# # print(v)



# #****************************Graphs

# import networkx as nx
# import matplotlib.pyplot as plt

# # Створюємо порожній граф
# G = nx.Graph()

# # Додаємо вершини
# G.add_node("A")
# G.add_node("B")
# G.add_node("C")

# # Додаємо з'єднання
# G.add_edge("A", "B")
# G.add_edge("B", "C")

# # Задаємо розташування вершин
# positions = {
#     "A": (0, 2.5),
#     "B": (-1, 4.5),
#     "C": (2, 0.5)
# }

# # Малюємо граф
# plt.figure(figsize=(6,6))
# nx.draw_networkx(G, pos=positions, with_labels=True, font_weight='bold', node_color='lightblue', edge_color='gray')
# plt.axis("on")
# plt.show()

name=1
v=f"ap #{name}"

print(v)