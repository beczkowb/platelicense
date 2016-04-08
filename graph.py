import sys
import string


def get_next_vertex(vertex, next_edge_value):
    for e in vertex.edges:
        if e.value == next_edge_value:
            return e.vertex


class Vertex:
    def __init__(self, edges, pk):
        self.edges = edges
        self.pk = pk

    def __str__(self):
        return '%d' % (self.pk, )


class Edge:
    def __init__(self, value, vertex):
        self.value = value
        self.vertex = vertex

    def __str__(self):
        return 'by %s to %s' % (self.vertex.pk, self.value)


# Helpful variables and functions
ascii_uppercase_and_digits = string.ascii_uppercase + '0123456789'
current_module = sys.modules[__name__]
generate_edges = lambda values, next_vertex: [Edge(value=c, vertex=next_vertex) for c in values]

# Creating graph
v8 = Vertex(pk=8, edges=[])
for i in range(7, 2, -1):
    prev_vertex = getattr(current_module, 'v%d' % (i + 1,))
    setattr(current_module, 'v%d' % i,
            Vertex(pk=i, edges=generate_edges(ascii_uppercase_and_digits, prev_vertex)))
v2 = Vertex(pk=2, edges=[Edge(value=c, vertex=getattr(current_module, 'v3')) for c in string.ascii_uppercase])
START = Vertex(pk=1, edges=generate_edges(string.ascii_uppercase, v2))
END = v8