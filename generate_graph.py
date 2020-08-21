import random


def generate_graph(num_of_node, num_of_edge):
    dic_sections_conflicts = {}
    for i in range(1, num_of_node+1):
        dic_sections_conflicts[i] = []
    for j in range(num_of_edge):
        flag = True
        while flag:
            node1 = random.randint(1, num_of_node)
            node2 = random.randint(1, num_of_node)
            if node1 != node2 and node2 not in dic_sections_conflicts[node1] and \
                    node1 not in dic_sections_conflicts[node2]:
                dic_sections_conflicts[node1].append(node2)
                flag = False
    return dic_sections_conflicts


# print(generate_graph(10000, 20000)[0])

