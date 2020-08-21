from data_structures import Vertices, Node, Linklist
from generate_graph import generate_graph
import random
import time


def radix_sort(to_be_sorted, max_degree):
  maximum_value = max_degree
  max_exponent = len(str(maximum_value))
  being_sorted = to_be_sorted[:]

  for exponent in range(max_exponent):
    position = exponent + 1
    index = -position

    digits = [[] for i in range(10)]

    for number in being_sorted:
      number_as_a_string = str(number.degree)
      try:
        digit = number_as_a_string[index]
      except IndexError:
        digit = 0
      digit = int(digit)

      digits[digit].append(number)

    being_sorted = []
    for numeral in digits:
      being_sorted.extend(numeral)

  return being_sorted[::-1]




def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i.degree <= pivot.degree]
        greater = [i for i in array[1:] if i.degree > pivot.degree]
        return quicksort(greater) + [pivot] + quicksort(less)


"""
Adjacent List
"""
smallest_vertex_last_ordering = []
# dic_sections_conflicts = {'A': ['B'], 'B': ['C', 'D'], 'C': ['D', 'E'], 'D': ['E', 'G'],
#                           'E': ['G', 'F'], 'F': ['G', 'I', 'H'], 'G': ['I', 'H'], 'H': ['I']}
dic_sections_conflicts = generate_graph(50000, 900000)
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


largest_degree = 0
for vertex in dic_vertices.keys():
    dic_vertices[vertex].degree = len(dic_vertices[vertex].adjacent_list)
    dic_vertices[vertex].degree_ori = len(dic_vertices[vertex].adjacent_list)
    if dic_vertices[vertex].degree > largest_degree:
        largest_degree = dic_vertices[vertex].degree

vertex_list = []
for vertex in dic_vertices.keys():
    vertex_list.append(dic_vertices[vertex])

# vertex_list_sorted = quicksort(vertex_list)
vertex_list_sorted = radix_sort(vertex_list, largest_degree)

for node in vertex_list_sorted:
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
# for node in vertex_list_sorted:
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
# print('Average original degree: ', original_degree_sum/len(vertex_list_sorted))
# print('Maximum degree when deleted: ', deleted_max_degree)

