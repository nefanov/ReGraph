import networkx as nx
import copy

from nose.tools import assert_equals

<<<<<<< HEAD
from regraph.library.data_structures import (TypedGraph,
                                             Homomorphism)
from regraph.library.category_op import (pullback, pushout, final_PBC)


def assert_edges_undir(edges1, edges2):
    assert_equals(len(edges1), len(edges2))
=======
from regraph.primitives import (get_relabeled_graph,
                                print_graph)
from regraph.utils import assert_graph_eq
from regraph.category_op import (pullback,
                                 pushout,
                                 pullback_complement,
                                 nary_pullback)


def assert_edges_undir(edges1, edges2):
>>>>>>> 943444f50b7c3af61e2938cd2b71d34782e6956c

    edgeset1 = set(edges1)
    edgeset2 = set(edges2)

    for edge in edgeset1:
        if edge not in edgeset2 and (edge[1], edge[0]) not in edgeset2:
            assert False


class TestCategoryOp:
    def __init__(self):
<<<<<<< HEAD
        D = TypedGraph()

        D.add_node('square', 'square')
        D.add_node('circle', 'circle')
        D.add_node('dark_square', 'dark_square')
        D.add_node('dark_circle', 'dark_circle')

        D.add_edge('square', 'circle')
        D.add_edge('circle', 'dark_circle')
        D.add_edge('circle', 'dark_square')
        D.add_edge('circle', 'circle')

        A = TypedGraph(D)

        A.add_node('circle', 'circle')
        A.add_node('dark_circle', 'dark_circle')

        A.add_edge('circle', 'dark_circle')

        B = TypedGraph(D)

        B.add_node(1, 'square')
        B.add_node(2, 'circle')
        B.add_node(3, 'dark_circle')

        B.add_edge(1, 2)
        B.add_edge(2, 3)

        C = TypedGraph(D)

        C.add_node('circle_circle', 'circle')
        C.add_node('dark_circle_dark_circle', 'dark_circle')
        C.add_node('dark_square_', 'dark_square')

        C.add_edge('circle_circle', 'dark_circle_dark_circle')
        C.add_edge('circle_circle', 'dark_square_')
        C.add_edge('circle_circle', 'circle_circle')

        dic_homAB = {
            'circle': 2,
            'dark_circle': 3
        }
        dic_homAC = {
            'circle': 'circle_circle',
            'dark_circle': 'dark_circle_dark_circle'
        }
        dic_homBD = {
=======
        D = nx.DiGraph()

        D.add_node('square')
        D.add_node('circle')
        D.add_node('dark_square')
        D.add_node('dark_circle')
        D.add_edge('square', 'circle')
        D.add_edge('circle', 'dark_circle')
        D.add_edge('circle', 'dark_square')
        D.add_edge('circle', 'circle')

        self.D = D

        A = nx.DiGraph()

        A.add_node(2)
        A.add_node(3)
        A.add_edge(2, 3)

        self.A = A

        B = nx.DiGraph()

        B.add_node(1)
        B.add_node(2)
        B.add_node(3)
        B.add_edge(1, 2)
        B.add_edge(2, 3)

        self.B = B

        C = nx.DiGraph()

        C.add_node(2)
        C.add_node(3)
        C.add_node('dark_square')

        C.add_edge(2, 3)
        C.add_edge(2, 'dark_square')
        C.add_edge(2, 2)

        self.C = C

        self.homAB = {
            2: 2,
            3: 3
        }
        self.homAC = {
            2: 2,
            3: 3
        }
        self.homBD = {
>>>>>>> 943444f50b7c3af61e2938cd2b71d34782e6956c
            1: 'square',
            2: 'circle',
            3: 'dark_circle'
        }

<<<<<<< HEAD
        dic_homCD = {
            'circle_circle': 'circle',
            'dark_circle_dark_circle': 'dark_circle',
            'dark_square_': 'dark_square'
        }

        self.homAB = Homomorphism(A, B, dic_homAB)
        self.homAC = Homomorphism(A, C, dic_homAC)
        self.homBD = Homomorphism(B, D, dic_homBD)
        self.homCD = Homomorphism(C, D, dic_homCD)

    def test_pullback(self):
        A, homAB, homAC = pullback(self.homBD, self.homCD)
        assert_equals(type(A), TypedGraph)
        assert_equals(A.nodes(), self.homAB.source_.nodes())
        assert_edges_undir(A.edges(), self.homAB.source_.edges())
        assert_equals(homAB.mapping_, self.homAB.mapping_)
        assert_equals(homAC.mapping_, self.homAC.mapping_)

    def test_final_PBC(self):
        C, homAC, homCD = final_PBC(self.homAB, self.homBD)
        assert_equals(type(C), TypedGraph)
        assert_equals(set(C.nodes()), set(self.homAC.target_.nodes()))
        assert_edges_undir(C.edges(), self.homAC.target_.edges())
        assert_equals(homAC.mapping_, self.homAC.mapping_)
        assert_equals(homCD.mapping_, self.homCD.mapping_)

    def test_pushout(self):
        D, homBD, homCD = pushout(self.homAB, self.homAC)
        assert_equals(type(D), TypedGraph)

        assert_equals(len(D.nodes()),
                      len(self.homBD.target_.nodes()))

        assert_equals(len(D.edges()),
                      len(self.homBD.target_.edges()))
=======
        self.homCD = {
            2: 'circle',
            3: 'dark_circle',
            'dark_square': 'dark_square'
        }

    def test_pullback(self):
        A, homAB, homAC = pullback(
            self.B, self.C, self.D, self.homBD, self.homCD,
        )
        assert_equals(type(A), nx.DiGraph)
        assert_equals(set(A.nodes()), set(self.A.nodes()))
        assert_edges_undir(A.edges(), self.A.edges())
        assert_equals(homAB, self.homAB)
        assert_equals(homAC, self.homAC)

    def test_pullback_complement(self):
        C, homAC, homCD = pullback_complement(
            self.A, self.B, self.D, self.homAB, self.homBD
        )
        assert_equals(type(C), nx.DiGraph)
        test_graph = get_relabeled_graph(
            self.C, {2: "circle", 3: "dark_circle", "dark_square": "dark_square"}
        )
        assert_graph_eq(test_graph, C)
        assert(id(self.D) != id(C))

    def test_pullpack_complement_inplace(self):
        D_copy = copy.deepcopy(self.D)
        C, homAC, homCD = pullback_complement(
            self.A, self.B, D_copy, self.homAB, self.homBD, inplace=True
        )
        assert_equals(type(C), nx.DiGraph)
        test_graph = get_relabeled_graph(
            self.C, {2: "circle", 3: "dark_circle", "dark_square": "dark_square"}
        )
        assert_graph_eq(test_graph, C)
        assert(id(D_copy) == id(C))

    def test_pushout(self):
        D, homBD, homCD = pushout(
            self.A, self.B, self.C, self.homAB, self.homAC
        )
        assert_equals(type(D), nx.DiGraph)

        assert_equals(len(D.nodes()),
                      len(self.D.nodes()))

        assert_equals(len(D.edges()),
                      len(self.D.edges()))
        assert(id(self.B) != id(D))

    def test_pushout_inplace(self):
        B_copy = copy.deepcopy(self.B)
        D, homBD, homCD = pushout(
            self.A, B_copy, self.C, self.homAB, self.homAC, inplace=True
        )
        assert_equals(type(D), nx.DiGraph)

        assert_equals(len(D.nodes()),
                      len(self.D.nodes()))

        assert_equals(len(D.edges()),
                      len(self.D.edges()))
        assert(id(B_copy) == id(D))

    def test_pushout_symmetry_directed(self):

        A = nx.DiGraph()
        A.add_nodes_from(["a", "b"])
        A.add_edges_from([("a", "b")])

        B = nx.DiGraph()
        B.add_nodes_from([1, 2, 3])
        B.add_edges_from([(2, 3), (3, 2), (1, 3)])

        C = nx.DiGraph()
        C.add_nodes_from(["x", "y"])
        C.add_edges_from([("x", "x"), ("x", "y")])

        homAB = {"a": 2, "b": 3}
        homAC = {"a": "x", "b": "x"}

        D, homBD, homCD = pushout(
            A, B, C, homAB, homAC
        )
        D_inv, homCD_inv, homBD_inv = pushout(
            A, C, B, homAC, homAB
        )
        assert_equals(len(D.nodes()), len(D_inv.nodes()))
        assert_equals(len(D.edges()), len(D_inv.edges()))

    def test_multi_pullback(self):
        B = nx.DiGraph()
        B.add_nodes_from([
            1,
            2,
            3,
            4,
            5
        ])
        B.add_edges_from([
            (1, 3),
            (2, 2),
            (3, 2),
            (4, 5),
            (5, 4)
        ])

        D1 = nx.DiGraph()
        D1.add_nodes_from(['c', 's'])
        D1.add_edges_from([('c', 's'), ('s', 'c'), ('c', 'c')])

        D2 = nx.DiGraph()
        D2.add_nodes_from(['b', 'w'])
        D2.add_edges_from([('b', 'b'), ('w', 'w')])

        D3 = nx.DiGraph()
        D3.add_nodes_from(['u', 'p'])
        D3.add_edges_from([('p', 'p'), ('p', 'u'), ('u', 'u')])

        b_d1 = {1: 'c', 2: 'c', 3: 's', 4: 'c', 5: 's'}
        b_d2 = {1: 'b', 2: 'b', 3: 'b', 4: 'w', 5: 'w'}
        b_d3 = {1: 'p', 2: 'u', 3: 'u', 4: 'p', 5: 'p'}

        C1 = nx.DiGraph()
        C1.add_nodes_from(['c1', 'c2', 's'])
        C1.add_edges_from([('c1', 's'), ('c2', 's'), ('c1', 'c1'), ('c2', 'c2')])
        c_d1 = {'c1': 'c', 'c2': 'c', 's': 's'}

        C2 = nx.DiGraph()
        C2.add_nodes_from(['b1', 'b2', 'w'])
        C2.add_edges_from([('b1', 'b1'), ('w', 'w')])
        c_d2 = {'b1': 'b', 'b2': 'b', 'w': 'w'}

        C3 = nx.DiGraph()
        C3.add_nodes_from(['u', 'p'])
        C3.add_edges_from([('p', 'u'), ('u', 'u'), ('p', 'p')])
        c_d3 = {'u': 'u', 'p': 'p'}

        A, A_B, A_Cs = nary_pullback(
            B,
            {'d1': (C1, D1, b_d1, c_d1),
             'd2': (C2, D2, b_d2, c_d2),
             'd3': (C3, D3, b_d3, c_d3)}
        )
        # print_graph(A)
        # print(A_B)
        # print(A_Cs)

    def test_multi_pullback_clones(self):
        B = nx.DiGraph()
        B.add_nodes_from([
            1,
        ])

        D1 = nx.DiGraph()
        D1.add_nodes_from(['a'])

        D2 = nx.DiGraph()
        D2.add_nodes_from(['x'])

        b_d1 = {1: 'a'}
        b_d2 = {1: 'x'}

        C1 = nx.DiGraph()
        C1.add_nodes_from(['a', 'a1'])

        C2 = nx.DiGraph()
        C2.add_nodes_from(['x', 'x1'])

        c_d1 = {'a': 'a', 'a1': 'a'}
        c_d2 = {'x': 'x', 'x1': 'x'}

        a, a_b, a_cs = nary_pullback(
            B,
            {
                'd1': (C1, D1, b_d1, c_d1),
                'd2': (C2, D2, b_d2, c_d2)
            }
        )
        # print(a_b)
        # print(a_cs)
>>>>>>> 943444f50b7c3af61e2938cd2b71d34782e6956c
