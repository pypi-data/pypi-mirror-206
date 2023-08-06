# -*- coding: utf-8 -*-
from graphdisplay import GraphGUI

class AdjacentVertex:
    """ This class allows us to represent a tuple
    with an adjacent vertex
    and the weight associated (by default None, for non-unweighted graphs)"""
    def __init__(self, vertex: object, weight: int = 1) -> None:
        self.vertex = vertex
        self.weight = weight

    def __str__(self) -> str:
        """ returns the tuple (vertex, weight)"""
        if self.weight is not None:
            return '(' + str(self.vertex) + ',' + str(self.weight) + ')'
        else:
            return str(self.vertex)

class Graph:
    def __init__(self, vertices: list, directed: bool = True) -> None:
        """ We use a dictionary to represent the graph
        the dictionary's keys are the vertices
        The value associated for a given key will be the list of their neighbours.
        Initially, the list of neighbours is empty"""
        self._vertices = {}
        for v in vertices:
            self._vertices[v] = []
        self._directed = directed

    def add_edge(self, start: object, end: object, weight: int = 1) -> None:
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return

        # adds to the end of the list of neighbours for start
        self._vertices[start].append(AdjacentVertex(end, weight))

        if not self._directed:
            # adds to the end of the list of neighbors for end
            self._vertices[end].append(AdjacentVertex(start, weight))

    def contain_edge(self, start: object, end: object) -> int:
        """ checks if the edge (start, end) exits. It does
        not exist return 0, eoc returns its weight or 1 (for unweighted graphs)"""
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return 0
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return 0

        # we search the AdjacentVertex whose v is equal to end
        for adj in self._vertices[start]:
            if adj.vertex == end:
                return adj.weight

        return 0  # does not exist

    def remove_edge(self, start: object, end: object):
        """ removes the edge (start, end)"""
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return

        # we must look for the adjacent AdjacentVertex (neighbour)  whose vertex is end, and then remove it
        for adj in self._vertices[start]:
            if adj.vertex == end:
                self._vertices[start].remove(adj)
        if not self._directed:
            # we must also look for the AdjacentVertex (neighbour)  whose vertex is end, and then remove it
            for adj in self._vertices[end]:
                if adj.vertex == start:
                    self._vertices[end].remove(adj)

    def __str__(self) -> str:
        """ returns a string containing the graph"""
        result = ''
        for v in self._vertices:
            result += '\n'+str(v)+':'
            for adj in self._vertices[v]:
                result += str(adj)+"  "
        return result

    def get_adjacents(self, vertex: object) -> list:
        """ returns a Python list containing the adjacent
        vertices of vertex. The list only contains the vertices"""
        if vertex not in self._vertices.keys():
            print(vertex, ' does not exist!')
            return None
        lst_adjacents = []
        for adj in self._vertices[vertex]:
            lst_adjacents.append(adj.vertex)
        return lst_adjacents

    def get_origins(self, vertex: object) -> list:
        """ returns a Python list containing those vertices that have
        an edge to vertex. The list is formed with objects of AdjacentVertex"""
        if vertex not in self._vertices.keys():
            print(vertex, ' does not exist!')
            return None
        lst_origins = []
        for v in self._vertices:
            for adj in self._vertices[v]:
                if vertex == adj.vertex:
                    lst_origins.append(v)
                    break
        return lst_origins


if __name__ == '__main__':

    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph(labels)

    # Now, we add the edges
    g.add_edge('A', 'C', 12)  # A->(12)C
    g.add_edge('A', 'D', 60)  # A->(60)D
    g.add_edge('B', 'A', 10)  # B->(10)A
    g.add_edge('C', 'B', 20)  # C->(20)B
    g.add_edge('C', 'D', 32)  # C->(32)D
    g.add_edge('E', 'A', 7)   # E->(7)A
    g.add_edge('A', 'E', 50)
    #GraphGUI(g)

    my_gragph = Graph(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'])
    my_gragph.add_edge('A', 'B', 4)
    my_gragph.add_edge('B', 'C', 8)
    my_gragph.add_edge('C', 'A', 100)
    my_gragph.add_edge('D', 'E', 7)
    my_gragph.add_edge('E', 'F', 10)
    my_gragph.add_edge('F', 'G', 5)
    my_gragph.add_edge('G', 'Z', 6)
    my_gragph.add_edge('A', 'H', 2)
    my_gragph.add_edge('B', 'I', 3)
    my_gragph.add_edge('C', 'J', 4)
    my_gragph.add_edge('D', 'K', 5)
    my_gragph.add_edge('E', 'L', 6)
    my_gragph.add_edge('F', 'D', 3)
    my_gragph.add_edge('G', 'H', 9)
    my_gragph.add_edge('H', 'Z', 2)
    my_gragph.add_edge('I', 'J', 1)
    my_gragph.add_edge('J', 'A', 6)
    my_gragph.add_edge('K', 'L', 5)
    my_gragph.add_edge('L', 'M', 4)
    my_gragph.add_edge('M', 'H', 3)
    my_gragph.add_edge('N', 'O', 2)
    my_gragph.add_edge('O', 'P', 1)
    my_gragph.add_edge('P', 'Q', 7)
    my_gragph.add_edge('H', 'A', 20)
    my_gragph.add_edge('K', 'B', 7)

    GraphGUI(my_gragph, 20, 800, 800)