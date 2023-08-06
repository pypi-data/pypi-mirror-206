"""
Directed edge data structure for triangle meshes

This module implements the directed edge data structure for triangle
meshes.

CLASSES
-------
mesh
    main class representing a triangle mesh
vertex
    a class representing a single mesh vertex
half_edge
    a class representing a single half edge
"""

from dataclasses import dataclass
from typing import Generator, Tuple
@dataclass
class vertex:
    """
    A class representing a mesh vertex

    Attributes
    ----------
    data : any
        user-defined data associated with the vertex
    half_edge : int
        index of a mesh half_edge starting at the vertex
    """

    data: any = None
    half_edge: int = -1


@dataclass
class half_edge:
    """A class representing a half_edge"""

    dst: int
    mate: int = -1


class mesh:
    """A class representing a triangle mesh

    This is an implementation of the Directed Edge data sructure for
    triangle meshes.

    Attributes
    ----------
    vertices : List[vertex]
        The list of all mesh vertices
    half_edges : List[half_edge]
        The list of all half edges in the mesh. Faces are coded by this
        list, so there is not need for a face container.

    Methods
    -------
    next(he: int) -> int
        returns the half edge next to he in the same face
    prev(he: int) -> int:
        returns the half edge previous to he in the same face
    face(he: int) -> int:
        returns the face to which half edge he belongs to
    vertex(self, v: int) -> vertex:
        returns the mesh vertex of index v
    half_edge(self, he: int) -> half_edge:
        returns the mesh half edge of index he
    number_of_vertices(self) -> int:
        returns the number of mesh vertices
    number_of_faces(self) -> int:
        returns the number of mesh faces
    vertex_neighbors(self, v: int):
        generator yielding the indices of vertices neighbors to vertex v
    vertex_neighboring_faces(self, v: int):
        generator yielding the indices of faces incident to vertex v
    face_neighbors(self, f: int):
        generator yielding the indices of faces neighbors to face f
    """

    def __init__(self, vertices, faces):
        self._vertices = [ vertex(v) for v in vertices ]
        self.half_edges = []
        self._half_edges_map = {}
        for f in faces:
            self.__add_face(f)
        for i in range(len(self._vertices)):
            self.__assert_vertex_half_edge(i)
        self._half_edges_map = None

    @staticmethod
    def next(he: int) -> int:
        if he % 3 == 2:
            return he - 2
        else:
            return  he + 1;

    @staticmethod
    def prev(he:int ) -> int:
        if he % 3 == 0:
            return he + 2
        else:
            return he - 1;

    @staticmethod
    def face(he: int) -> int:
        return int(he/3)

    def vertex(self, v: int) -> vertex:
        return self._vertices[v]

    def half_edge(self, he: int) -> half_edge:
        return self.half_edges[he]

    def number_of_vertices(self) -> int:
        return len(self._vertices)

    def number_of_faces(self) -> int:
        return int(len(self.half_edges)/3)

    def vertex_neighbors(self, v: int) -> Generator[int, None, None]:
        h = -1
        for he in self.vertex_halfedges(v):
            yield self.half_edge(he).dst
            h = he
        if h > -1 and self.half_edge(self.prev(h)).mate == -1: #bordo
            yield self.half_edge(self.next(h)).dst

    def vertex_halfedges(self, v: int) -> Generator[int, None, None]:
        he = self.vertex(v).half_edge
        if he != -1:
            hn = he
            while True:
                yield hn
                hn = self.half_edge(self.prev(hn)).mate
                if hn in {-1, he}:
                    break

    def vertex_faces(self, v: int) -> Generator[int, None, None]:
        for he in self.vertex_halfedges(v):
            yield self.face(he)

    def face_neighbors(self, f: int) -> Generator[int, None, None]:
        hf = 3*f
        for i in range(3):
            h = hf+i
            mate = self.half_edge(h).mate
            if mate > -1:
                yield self.face(mate)

    def faces(self) -> Generator[Tuple[int, int, int], None, None]:
        for f in range(self.number_of_faces()):
            i = self.half_edge(3*f).dst
            j = self.half_edge(3*f+1).dst
            k = self.half_edge(3*f+2).dst
            yield (i, j, k)

    def vertices(self) -> Generator[any, None, None]:
        for v in self._vertices:
            yield v.data

    def __add_face(self, f: any) -> None:
        self.__put_half_edge(f[0], f[1])
        self.__put_half_edge(f[1], f[2])
        self.__put_half_edge(f[2], f[0])

    def __put_half_edge(self, vi: int, vj: int) -> None:
        pair = (vi, vj)
        if pair in self._half_edges_map:
            print("Error  : wrong orientation on mesh. Quitting ...")
            exit()
        h = len(self.half_edges)
        he = half_edge(vj)
        self.half_edges.append(he)
        if self._vertices[vi].half_edge == -1:
            self._vertices[vi].half_edge = h
        self._half_edges_map[pair] = h
        other_pair = (vj, vi)
        if other_pair in self._half_edges_map:
            self.__link(h, self._half_edges_map[other_pair]);

    def __link(self, he1: int, he2: int) -> None:
        if he1 != -1:
            self.half_edges[he1].mate = he2
        if he2 != -1:
            self.half_edges[he2].mate = he1

    def __assert_vertex_half_edge(self, v: int) -> None:
        first = self._vertices[v].half_edge
        if first != -1:
            mate  = self.half_edges[first].mate
            if mate != -1:
                current = self.next(mate)
                while current != first:
                    mate = self.half_edges[current].mate
                    if mate != -1:
                        current = self.next(mate)
                    else:
                        self._vertices[v].half_edge = current
                        current = first
        else:
            print("Warning : vetex %d is isolated." % v)
