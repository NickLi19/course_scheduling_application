from data_structures import Vertices, Node, Linklist
from generate_graph import generate_graph
import random
import time

"""
Adjacent List
"""
smallest_vertex_last_ordering = []
# dic_sections_conflicts = {'A': ['B'], 'B': ['C', 'D'], 'C': ['D', 'E'], 'D': ['E', 'G'],
#                           'E': ['G', 'F'], 'F': ['G', 'I', 'H'], 'G': ['I', 'H'], 'H': ['I']}
dic_sections_conflicts = generate_graph(400000, 1000)
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

for vertex in dic_vertices.keys():
    dic_vertices[vertex].degree = len(dic_vertices[vertex].adjacent_list)
    dic_vertices[vertex].degree_ori = len(dic_vertices[vertex].adjacent_list)

vertex_list = []
for vertex in dic_vertices.keys():
    vertex_list.append(dic_vertices[vertex])
random.shuffle(vertex_list)

# for vertex in vertex_list:
#     node_ordering = Node_ordering(vertex.section, vertex)
#     smallest_vertex_last_ordering.append(node_ordering)

for node in vertex_list:
    cur_node = node.adjacent_list.head
    largest_color = 1
    color = []
    while cur_node:
        color.append(cur_node.original_section.color)
        cur_node = cur_node._next
    color.sort()
    for node_color in color:
        if node_color == largest_color:
            largest_color += 1
    node.color = largest_color
end_time = time.time()
running_time = end_time - start_time
print('The running time for Smallest Vertex Last Ordering is: %f' % running_time)

# color_dic = {}
# number_of_color = 0
# max_degree = 0
# original_degree_sum = 0
# deleted_max_degree = 0
# for node in vertex_list:
#     print('-------------------')
#     print('Section:', node.section)
#     print('Degree when deleted: ', node.degree)
#     print('Original Degree: ', node.degree_ori)
#     print('Color: ', node.color)
#     if node.color not in color_dic:
#         color_dic[node.color] = 1
#         number_of_color += 1
#     if node.degree > deleted_max_degree:
#         deleted_max_degree = node.degree
#     original_degree_sum += node.degree_ori
# print('------------------------------')
# print('Total number of color: ', number_of_color)
# print('Average original degree: ', original_degree_sum/len(vertex_list))
# print('Maximum degree when deleted: ', deleted_max_degree)
#
