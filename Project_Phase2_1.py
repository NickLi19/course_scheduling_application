from data_structures import Vertices, Node, NodeDegree, Linklist, Circular_Double_Linked_List, Node_ordering
import matplotlib.pyplot as plt
from generate_graph import generate_graph
import time

"""
Adjacent List
"""
smallest_vertex_last_ordering = []
dic_sections_conflicts = {'A': ['B'], 'B': ['C', 'D'], 'C': ['D', 'E'], 'D': ['E', 'G'],
                          'E': ['G', 'F'], 'F': ['G', 'I', 'H'], 'G': ['I', 'H'], 'H': ['I'], 'Z': []}
# dic_sections_conflicts = generate_graph(1000, 12000)

start_time = time.time()
dic_vertices = {}
for section in dic_sections_conflicts.keys():
    if section not in dic_vertices:
        adjacent_list = Linklist()
        vertex = Vertices(section=section, adjacent_list=adjacent_list)
        dic_vertices[section] = vertex
    for section_conflict in dic_sections_conflicts[section]:
        if section_conflict not in dic_vertices:
            adjacent_list_conflict = Linklist()
            vertex_conflict = Vertices(section=section_conflict, adjacent_list=adjacent_list_conflict)
            dic_vertices[section_conflict] = vertex_conflict

        adjacent_node = Node(section=section_conflict, original_section=dic_vertices[section_conflict])
        dic_vertices[section].adjacent_list.append(adjacent_node)

        adjacent_node_original = Node(section=section, original_section=dic_vertices[section])
        dic_vertices[section_conflict].adjacent_list.append(adjacent_node_original)

# for vertex in dic_vertices.keys():
#     print('-------------------------')
#     print('Section_Dic: ', dic_vertices[vertex].section)
#     print('Display:')
#     dic_vertices[vertex].adjacent_list.display()

"""
Degree List
"""
largest_degree = float("-inf")
for vertex in dic_vertices.keys():
    dic_vertices[vertex].degree = len(dic_vertices[vertex].adjacent_list)
    dic_vertices[vertex].degree_ori = len(dic_vertices[vertex].adjacent_list)
    temp_degree = len(dic_vertices[vertex].adjacent_list)
    if temp_degree > largest_degree:
        largest_degree = temp_degree
dic_degrees = [Circular_Double_Linked_List() for _ in range(largest_degree+1)]

for vertex in dic_vertices.keys():
    degree_node = NodeDegree(section=dic_vertices[vertex].section, original_section=dic_vertices[vertex])
    dic_degrees[dic_vertices[vertex].degree].append(degree_node)
    dic_vertices[vertex].section_degree = degree_node
    dic_vertices[vertex].degree_list = dic_degrees[dic_vertices[vertex].degree]


# for degree in range(len(dic_degrees)):
#     print('-------------------------')
#     print('Degree: ', degree)
#     print('Display:')
#     dic_degrees[degree].display()

"""
Deleting Nodes From Degree List
"""
smallest_degree_list = float("inf")
not_delete_all = True
for degree in range(len(dic_degrees)):
    if len(dic_degrees[degree]) > 0 and degree < smallest_degree_list:
        smallest_degree_list = degree

while not_delete_all:
    node_delete = dic_degrees[smallest_degree_list].root.next
    node_delete.original_section.delete = True
    current_node = node_delete.original_section.adjacent_list.head
    while current_node:
        if not current_node.original_section.delete:
            current_node.original_section.degree -= 1
            new_degree_node = current_node.original_section.degree_list.remove(current_node.original_section.section_degree)
            dic_degrees[current_node.original_section.degree].append(new_degree_node)
            current_node.original_section.degree_list = dic_degrees[current_node.original_section.degree]
        current_node = current_node._next

    node_ordering = Node_ordering(node_delete.section, node_delete.original_section)
    dic_degrees[smallest_degree_list].popleft()
    smallest_vertex_last_ordering.append(node_ordering)

    start = smallest_degree_list
    smallest_degree_list = float("inf")
    not_delete_all = False
    for degree in range(start-1, len(dic_degrees)):
        if degree >= 0:
            if len(dic_degrees[degree]) > 0 and degree < smallest_degree_list:
                smallest_degree_list = degree
                not_delete_all = True
                break

# for node in smallest_vertex_last_ordering[::-1]:
#     print(node.section)
#     print(node.original_section.degree)

for node in smallest_vertex_last_ordering[::-1]:
    cur_node = node.original_section.adjacent_list.head
    largest_color = 1
    color = []
    while cur_node:
        color.append(cur_node.original_section.color)
        cur_node = cur_node._next
    color.sort()
    for node_color in color:
        if node_color == largest_color:
            largest_color += 1
    node.original_section.color = largest_color

end_time = time.time()
running_time = end_time - start_time
print('The running time for Smallest Vertex Last Ordering is: %f' % running_time)
# for node in smallest_vertex_last_ordering[::-1]:
#     print('-------------------')
#     print('Section:', node.section)
#     print('Degree: ', node.original_section.degree)
#     print('Original Degree: ', node.original_section.degree_ori)
#     print('Color', node.original_section.color)

color_dic = {}
number_of_color = 0
max_degree = 0
original_degree_sum = 0
deleted_max_degree = 0
y_axis = []
x_axis = []
for node in smallest_vertex_last_ordering[::-1]:
    x_axis.append(node.section)
    y_axis.append(node.original_section.degree)
    print('-------------------')
    print('Section:', node.section)
    print('Degree: ', node.original_section.degree)
    print('Original Degree: ', node.original_section.degree_ori)
    print('Color', node.original_section.color)
    if node.original_section.color not in color_dic:
        color_dic[node.original_section.color] = 1
        number_of_color += 1
    if node.original_section.degree > deleted_max_degree:
        deleted_max_degree = node.original_section.degree
    original_degree_sum += node.original_section.degree_ori

print('------------------------------')
print('Total number of color: ', number_of_color)
print('Average original degree: ', original_degree_sum/len(smallest_vertex_last_ordering))
print('Maximum degree when deleted: ', deleted_max_degree)

size_of_terminal_clique = -1
for node in smallest_vertex_last_ordering[::-1]:
    if node.original_section.degree > size_of_terminal_clique:
        size_of_terminal_clique += 1
    else:
        break
print('Size of terminal clique: ', size_of_terminal_clique+1)


def plot_histogram(x, y):
    plt.bar(x, y, facecolor='blue', width=3)
    plt.xlabel('Course')
    plt.ylabel('Smallest Vertex Last Ordering')
    plt.title('Degree when deleted')
    plt.legend()
    plt.show()
plot_histogram(x_axis, y_axis)

