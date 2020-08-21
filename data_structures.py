class Vertices:
    def __init__(self, section, adjacent_list=None, degree_list=None, section_degree=None, degree=0, degree_ori=0,
                 color=0, delete=False):
        self.section = section
        self.adjacent_list = adjacent_list
        self.degree_list = degree_list
        self.section_degree = section_degree
        self.degree = degree
        self.degree_ori = degree_ori
        self.color = color
        self.delete = delete

    def __repr__(self):
        return str(self.section)  # Need reconsider


class Node:
    def __init__(self, section, pnext=None, original_section=None):
        self.section = section
        self._next = pnext
        self.original_section = original_section

    def __repr__(self):
        return str(self.section)  # Need reconsider


class Linklist(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def isEmpty(self):
        return (self.length == 0)

    def append(self, section):
        item = section
        if self.tail == None:
            self.head = item
            self.tail = item
            self.length += 1

        else:
            item._next = None
            self.tail._next = item
            self.tail = item
            self.length += 1

    def display(self):
        cur = self.head
        while cur:
            print('Section: ', cur.section)
            print('Original_section: ', cur.original_section.section)
            print('Original_section_degree: ', cur.original_section.degree)
            cur = cur._next


class NodeDegree:

    def __init__(self, section=None, original_section=None):
        self.section = section
        self.original_section = original_section
        self.next, self.prev = None, None


class Circular_Double_Linked_List(object):

    def __init__(self, maxsize=None):
        self.root = NodeDegree()
        self.root.next = self.root
        self.root.prev = self.root
        self.count = 0
        self.maxsize = maxsize

    def __len__(self):
        return self.count

    def append(self, section):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("Linked List Full")
        node = section
        tailnode = self.root.prev
        tailnode.next = node
        node.next = self.root
        self.root.prev = node
        node.prev = tailnode
        self.count += 1

    def remove(self, node):
        if node is self.root:
            raise Exception('remove empty Liked List')
        prevnode = node.prev
        nextnode = node.next
        prevnode.next = nextnode
        nextnode.prev = prevnode
        node.prev = None
        node.next = None
        self.count -= 1
        return node

    def popleft(self):
        if self.root.next is self.root:
            raise Exception('pop from a empty linked list')
        headnode = self.root.next
        self.root.next = headnode.next
        headnode.next.prev = self.root
        section = headnode.section
        del headnode
        self.count -= 1
        return section

    def display(self):
        cur = self.root.next
        while cur != self.root:
            print('Section: ', cur.section)
            print('Original Section: ', cur.original_section.section)
            cur = cur.next


class Node_ordering:

    def __init__(self, section, original_section=None):
        self.section = section
        self.original_section = original_section

    def __repr__(self):
        return str(self.section)  # Need reconsider
