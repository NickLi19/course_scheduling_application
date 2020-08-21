import random
import time
import matplotlib.pyplot as plt
from data_structures import Vertices, Node, NodeDegree, Linklist, Circular_Double_Linked_List, Node_ordering


class Course(object):
    def __init__(self, course_num, section_num):
        self.course_num = course_num
        self.section_num = section_num
        self.name = str(self.course_num) + '-' + str(self.section_num)

    def __repr__(self):
        des = str(self.course_num) + '-' + str(self.section_num)
        return des  # Need reconsider


def plot_histogram(x, y):
    plt.bar(x, y, facecolor='blue', width=3)
    plt.xlabel('Course')
    plt.ylabel('Number of students')
    plt.xlim((1, C))
    plt.title('Distribution of courses among students')
    plt.legend()
    plt.show()


C = int(input('Please enter the number of courses being offered: '))
while C < 1 or C > 10000:
    C = int(input('The range of number of courses is [1, 10,000], please enter a valid number: '))
S = int(input('Please enter the number of students: '))
while S < 1 or S > 100000:
    S = int(input('The range of number of students is [1, 100,000], please enter a valid number: '))
K = int(input('Please enter the number of courses per student: '))
while K < 1 or K > C:
    K = int(input('The range of number of courses per student is [1, %d], please enter a valid number: ' % C))
SectionSize = int(input('Please enter the target size of a section: '))

print('The number of Courses(C): %d' % C)
print('The number of Students(S): %d' % S)
print('The number of courses for each student(K): %d' % K)
print('Section Size: %d' % SectionSize)

course_list = [i for i in range(1, C+1)]
course_count = [0] * (C+1)
students_dic = {}
course_dic = {}


def uniform_distribution(course_list, K):
    course_list_temp = [x for x in course_list]
    result = []
    for i in range(K):
        index = random.randint(i, len(course_list_temp)-1)
        course_list_temp[i], course_list_temp[index] = course_list_temp[index], course_list_temp[i]
        result.append(course_list_temp[i])
    return result


"""Uniform Distribution"""
start_time = time.time()
for i in range(1, S+1):
    students_dic[i] = uniform_distribution(course_list, K)
end_time = time.time()
running_time = end_time - start_time
print('The running time for uniform distribution is: %f' % running_time)

for student in students_dic.keys():
    for course in students_dic[student]:
        course_count[course] += 1
        if course not in course_dic:
            course_dic[course] = [student]
        else:
            course_dic[course] += [student]
plot_histogram(course_list, course_count[1:])


"""Two Tiered Distribution"""
course_rate_list = [i for i in range(1, K*10+1)]
start_time = time.time()
for i in range(1, S+1):
    course_random_rate = uniform_distribution(course_rate_list, K)
    first_tiered = 0
    second_tiered = 0
    for random_rate in course_random_rate:
        if random_rate <= int(K*5):
            first_tiered += 1
        else:
            second_tiered += 1
    pivot = int(C / 10) + 1
    course_first_tiered = uniform_distribution(course_list[:pivot], first_tiered)
    course_second_tiered = uniform_distribution(course_list[pivot:], second_tiered)
    students_dic[i] = course_first_tiered + course_second_tiered
end_time = time.time()
running_time = end_time - start_time
print('DIST: 2-TIERED')
print('The running time for two-tiered distribution is: %f' % running_time)

for student in students_dic.keys():
    for course in students_dic[student]:
        course_count[course] += 1
        if course not in course_dic:
            course_dic[course] = [student]
        else:
            course_dic[course] += [student]
plot_histogram(course_list, course_count[1:])

"""Four Tiered Distribution"""
course_rate_list = [i for i in range(1, K*10)]
start_time = time.time()
for i in range(1, S+1):
    course_random_rate = uniform_distribution(course_rate_list, K)
    first_tiered = 0
    second_tiered = 0
    third_tiered = 0
    fourth_tiered = 0
    for random_rate in course_random_rate:
        if random_rate <= int(K*10*0.4):
            first_tiered += 1
        elif random_rate <= int(K*10*0.7):
            second_tiered += 1
        elif random_rate <= int(K*10*0.9):
            third_tiered += 1
        else:
            fourth_tiered += 1
    pivot1 = int(C / 4) + 1
    pivot2 = int(C / 2) + 1
    pivot3 = int(C * 3 / 4) + 1
    course_first_tiered = uniform_distribution(course_list[:pivot1], first_tiered)
    course_second_tiered = uniform_distribution(course_list[pivot1: pivot2], second_tiered)
    course_third_tiered = uniform_distribution(course_list[pivot2: pivot3], third_tiered)
    course_fourth_tiered = uniform_distribution(course_list[pivot3:], fourth_tiered)
    students_dic[i] = course_first_tiered + course_second_tiered + course_third_tiered + course_fourth_tiered
end_time = time.time()
running_time = end_time - start_time
print('DIST: 4-TIERED')
print('The running time for four-tiered distribution is: %f' % running_time)


for student in students_dic.keys():
    for course in students_dic[student]:
        course_count[course] += 1
        if course not in course_dic:
            course_dic[course] = [student]
        else:
            course_dic[course] += [student]
plot_histogram(course_list, course_count[1:])


"""Three Tiered of Splitting"""
course_rate_list = [i for i in range(1, K*10)]
start_time = time.time()
for i in range(1, S+1):
    course_random_rate = uniform_distribution(course_rate_list, K)
    first_tiered = 0
    second_tiered = 0
    third_tiered = 0
    for random_rate in course_random_rate:
        if random_rate <= int(K*10*0.5):
            first_tiered += 1
        elif random_rate <= int(K*10*0.8):
            second_tiered += 1
        else:
            third_tiered += 1
    pivot1 = int(C * 0.15) + 1
    pivot2 = int(C / 2) + 1
    course_first_tiered = uniform_distribution(course_list[:pivot1], first_tiered)
    course_second_tiered = uniform_distribution(course_list[pivot1: pivot2], second_tiered)
    course_third_tiered = uniform_distribution(course_list[pivot2:], third_tiered)
    students_dic[i] = course_first_tiered + course_second_tiered + course_third_tiered
end_time = time.time()
running_time = end_time - start_time
print('DIST: 3-TIERED Distribution(My approach)')
print('The running time for three-tiered distribution is: %f' % running_time)


for student in students_dic.keys():
    for course in students_dic[student]:
        course_count[course] += 1
        if course not in course_dic:
            course_dic[course] = [student]
        else:
            course_dic[course] += [student]
plot_histogram(course_list, course_count[1:])


"""Simple way of splitting"""
student_dic_sections = {}
course = 1
start_time = time.time()
for course_size in course_count[1:]:
    section_size_each = int(SectionSize * 2 / 3)
    sections_num = int(course_size / section_size_each)

    if sections_num >= 1:
        multi = 1
        while multi <= sections_num:
            course_section = Course(course, multi)
            start = (multi-1) * section_size_each
            if multi == sections_num:
                end = course_size
            else:
                end = multi*section_size_each
            for student in course_dic[course][start:end]:
                if student not in student_dic_sections:
                    student_dic_sections[student] = [course_section]
                else:
                    student_dic_sections[student] += [course_section]
            multi += 1
    else:
        course_section = Course(course, 1)
        for student in course_dic[course][:course_size]:
            if student not in student_dic_sections:
                student_dic_sections[student] = [course_section]
            else:
                student_dic_sections[student] += [course_section]

    course += 1
end_time = time.time()
running_time = end_time - start_time
print('Split: BASIC')
print('The running time for simple way of splitting is: %f' % running_time)


"""Advanced way of splitting"""
student_dic_sections = {}
course = 1
start_time = time.time()
for course_size in course_count[1:]:
    section_size_each = int(SectionSize * 4 / 3)
    sections_num = int(course_size / section_size_each)

    if sections_num >= 1:
        multi = 1
        end_flag = False
        while multi <= sections_num:
            course_section = Course(course, multi)
            start = (multi-1) * section_size_each
            if multi == sections_num:
                end = start + int(section_size_each / 2)
                end_flag = True
            else:
                end = multi*section_size_each
            for student in course_dic[course][start:end]:
                if student not in student_dic_sections:
                    student_dic_sections[student] = [course_section]
                else:
                    student_dic_sections[student] += [course_section]
            if end_flag:
                for student in course_dic[course][end:course_size]:
                    if student not in student_dic_sections:
                        student_dic_sections[student] = [course_section]
                    else:
                        student_dic_sections[student] += [course_section]
            multi += 1
    else:
        course_section = Course(course, 1)
        if course_dic.get(course):
            for student in course_dic[course][:course_size]:
                if student not in student_dic_sections:
                    student_dic_sections[student] = [course_section]
                else:
                    student_dic_sections[student] += [course_section]

    course += 1
end_time = time.time()
running_time = end_time - start_time
print('Split: BASIC')
print('The running time for advanced way of splitting is: %f' % running_time)


"""Removing Duplicates"""
T = 0
M = 0
E = []
P = []
dic_remove_duplicate = {}
dic_sections_conflicts = {}
start_time = time.time()
for student in student_dic_sections.keys():
    for idx, section_outer in enumerate(student_dic_sections[student]):
        for section_inner in student_dic_sections[student][idx+1:]:
            T += 1
            conflict_pair = (section_outer, section_inner)
            if conflict_pair not in dic_remove_duplicate:
                M += 1
                dic_remove_duplicate[conflict_pair] = 1
                if conflict_pair[0] not in dic_sections_conflicts:
                    dic_sections_conflicts[conflict_pair[0]] = [conflict_pair[1]]
                else:
                    dic_sections_conflicts[conflict_pair[0]] += [conflict_pair[1]]
end_time = time.time()
running_time = end_time - start_time
print('The running time for removing duplicated is: %f' % running_time)

P_section = []
e_index = 0
for section in dic_sections_conflicts.keys():
    P_section.append(section)
    P.append(e_index)
    length = 0
    for section_conflict in dic_sections_conflicts[section]:
        length += 1
        E.append(section_conflict)
    e_index += length

print('Total conflicts is(T): %d' % T)
print('Distinct conflicts is(M): %d' % M)

print('----------------------------------------------Part II------------------------------------------------------')

smallest_vertex_last_ordering = []
# dic_sections_conflicts = {'A': ['B'], 'B': ['C', 'D'], 'C': ['D', 'E'], 'D': ['E', 'G'],
#                           'E': ['G', 'F'], 'F': ['G', 'I', 'H'], 'G': ['I', 'H'], 'H': ['I']}
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
# Degree List
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
# Deleting Nodes From Degree List
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
    for degree in range(start-2, len(dic_degrees)):
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

# for node in smallest_vertex_last_ordering[::-1]:
#     print('-------------------')
#     print('Section:', node.section)
#     print('Degree: ', node.original_section.degree)
#     print('Original Degree: ', node.original_section.degree_ori)
#     print('Color', node.original_section.color)
# print(dic_degrees[0])
color_dic = {}
number_of_color = 0
max_degree = 0
original_degree_sum = 0
deleted_max_degree = 0
y_axis = []
x_axis = []
for node in smallest_vertex_last_ordering[::-1]:
    x_axis.append(node.section.name)
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
    plt.ylabel('Degree when deleted')
    plt.title('Smallest Vertex Last Ordering')
    plt.legend()
    plt.show()


plot_histogram(x_axis, y_axis)


################################################## Random Vertex Ordering #############################################

smallest_vertex_last_ordering = []
# dic_sections_conflicts = {'A': ['B'], 'B': ['C', 'D'], 'C': ['D', 'E'], 'D': ['E', 'G'],
#                           'E': ['G', 'F'], 'F': ['G', 'I', 'H'], 'G': ['I', 'H'], 'H': ['I']}
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


color_dic = {}
number_of_color = 0
max_degree = 0
original_degree_sum = 0
deleted_max_degree = 0
y_axis = []
x_axis = []
for node in vertex_list:
    x_axis.append(node.section.name)
    y_axis.append(node.degree)
    print('-------------------')
    print('Section:', node.section)
    print('Degree when deleted: ', node.degree)
    print('Original Degree: ', node.degree_ori)
    print('Color: ', node.color)
    if node.color not in color_dic:
        color_dic[node.color] = 1
        number_of_color += 1
    if node.degree > deleted_max_degree:
        deleted_max_degree = node.degree
    original_degree_sum += node.degree_ori
print('------------------------------')
print('Total number of color: ', number_of_color)
print('Average original degree: ', original_degree_sum/len(vertex_list))
print('Maximum degree when deleted: ', deleted_max_degree)


def plot_histogram(x, y):
    plt.bar(x, y, facecolor='blue', width=3)
    plt.xlabel('Section')
    plt.ylabel('Random Ordering')
    plt.title('Degree when deleted')
    plt.legend()
    plt.show()


plot_histogram(x_axis, y_axis)


############################## Largest Degree First Vertex Ordering ###############################
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
# dic_sections_conflicts = generate_graph(50000, 900000)
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

color_dic = {}
number_of_color = 0
max_degree = 0
original_degree_sum = 0
deleted_max_degree = 0
y_axis = []
x_axis = []
for node in vertex_list_sorted:
    x_axis.append(node.section.name)
    y_axis.append(node.degree)
    print('Section:', node.section)
    print('Degree when deleted: ', node.degree)
    print('Original Degree: ', node.degree_ori)
    print('Color: ', node.color)
    if node.color not in color_dic:
        color_dic[node.color] = 1
        number_of_color += 1
    if node.degree > deleted_max_degree:
        deleted_max_degree = node.degree
    original_degree_sum += node.degree_ori
print('------------------------------')
print('Total number of color: ', number_of_color)
print('Average original degree: ', original_degree_sum/len(vertex_list_sorted))
print('Maximum degree when deleted: ', deleted_max_degree)


def plot_histogram(x, y):
    plt.bar(x, y, facecolor='blue', width=3)
    plt.xlabel('Course')
    plt.ylabel('Degree when deleted')
    plt.title('Largest Degree First Vertex Ordering')
    plt.legend()
    plt.show()


plot_histogram(x_axis, y_axis)