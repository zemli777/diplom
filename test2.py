import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

from pars_file import Get_adjacency_matrix
from pars_file import Post_adjacency_matrix
from pars_file import matrix_nx
from dir_create import dir_graf
from base import all_db, add_to_db, dell_from_db_from_name, dell_from_db_drom_path, find_db_from_path, \
    find_db_from_name, edit_db_name

class Graph:

    def __init__(self, name, list):
        self.name = name
        self.list = list
        self.n = 0

    def update_name(self, name):
        self.name = name

    def update_list(self, list):
        self.list

    def graph_update(path, list):
        adj = Post_adjacency_matrix(path, list)
        adj_max = Get_adjacency_matrix(path)
        G = nx.DiGraph(np.matrix(adj_max))

        nx.draw(G, pos=nx.planar_layout(G), with_labels=True, node_size=500, arrows=True)

        # plt.show()
        # os.remove(f'{path}.png')
        plt.savefig(path)
        plt.close()


    def graph_build(self, path, list):
        adj = Post_adjacency_matrix(path, list)
        adj_max = Get_adjacency_matrix(path)

        G = nx.DiGraph(np.matrix(adj_max))
        nx.draw(G, pos=nx.planar_layout(G), with_labels=True, node_size=500, arrows=True)
        # plt.show()
        plt.savefig(path)
        plt.close()
        self.n += 1
        add_to_db(f'graph{self.n}', path)


    def operation_sum(path1, path2, path3):
        adj_max = Get_adjacency_matrix(path1)

        G = nx.DiGraph(np.matrix(adj_max))
        adj_max = Get_adjacency_matrix(path2)
        H = nx.DiGraph(np.matrix(adj_max))

        R = nx.compose(G, H)
        matrix = matrix_nx(nx.to_numpy_array(R))
        Post_adjacency_matrix(path3, matrix)
        plt.savefig(path3)


    def operation_multiplication(path1, path2, path3):
        adj_max = Get_adjacency_matrix(path1)

        G = nx.DiGraph(np.matrix(adj_max))

        adj_max = Get_adjacency_matrix(path2)
        H = nx.DiGraph(np.matrix(adj_max))

        R = nx.intersection(G, H)
        matrix = matrix_nx(nx.to_numpy_array(R))
        Post_adjacency_matrix(path3, matrix)
        plt.savefig(path3)
        plt.close()


    def operation_not_edges(path):
        adj_max = Get_adjacency_matrix(path)

        G = nx.DiGraph(np.matrix(adj_max))
        G = nx.complement(G)
        # nx.draw(G, pos=nx.planar_layout(G), with_labels=True, node_size=500, arrows=True)
        # plt.show()
        matrix = matrix_nx(nx.to_numpy_array(G))
        Post_adjacency_matrix(path, matrix)
        plt.close()


    def operation_composition(path1, path2, path3, path4):
        adj_max = Get_adjacency_matrix(path1)

        G = nx.DiGraph(np.matrix(adj_max))

        adj_max = Get_adjacency_matrix(path2)

        H = nx.DiGraph(np.matrix(adj_max))
        F = nx.cartesian_product(G, H)
        R = nx.lexicographic_product(G, H)
        matrix = matrix_nx(nx.to_numpy_array(R))
        Post_adjacency_matrix(path3, matrix)
        plt.savefig(path4)
        plt.savefig(path3)
        plt.close()


    def operation_add_node(path, x):
        adj_max = Get_adjacency_matrix(path)

        G = nx.DiGraph(np.matrix(adj_max))
        G.add_node(x)
        matrix = matrix_nx(nx.to_numpy_array(G))
        Post_adjacency_matrix(path, matrix)
        plt.close()


    def operation_add_edge(path, x, y):
        adj_max = Get_adjacency_matrix(path)

        G = nx.DiGraph(np.matrix(adj_max))
        G.add_edge(x, y)
        matrix = matrix_nx(nx.to_numpy_array(G))
        Post_adjacency_matrix(path, matrix)
        plt.close()


    def operation_delete_node(path, x):
        adj_max = Get_adjacency_matrix(path)

        G = nx.DiGraph(np.matrix(adj_max))
        G.remove_node(x)
        matrix = matrix_nx(nx.to_numpy_array(G))
        Post_adjacency_matrix(path, matrix)
        plt.close()


    def operation_delete_edge(path, x, y):
        adj_max = Get_adjacency_matrix(path)

        G = nx.DiGraph(np.matrix(adj_max))
        G.remove_edge(x, y)
        matrix = matrix_nx(nx.to_numpy_array(G))
        Post_adjacency_matrix(path, matrix)
        plt.close()


    def operation_contraction_edge(self, path, x, y):
        adj_max = Get_adjacency_matrix(path)

        G = nx.DiGraph(np.matrix(adj_max))

        nx.draw(G, pos=nx.planar_layout(G), with_labels=True, node_size=500, arrows=True)
        plt.show()

        neibx = []
        neiby = []

        for i in nx.neighbors(G, x):
            neibx.append(i)

        for i in nx.neighbors(G, y):
            neiby.append(i)

        d = list(set(neibx) & set(neiby))
        c = list(set(neibx + neiby))
        self.operation_delete_node(path, y)

        for i in d:
            self.operation_add_edge(path, x, i)
            print('add', i)

        adj_max = Get_adjacency_matrix(path)

        G = nx.DiGraph(np.matrix(adj_max))

        nx.draw(G, pos=nx.planar_layout(G), with_labels=True, node_size=500, arrows=True)
        plt.show()
        plt.close()
        # matrix = matrix_nx(nx.to_numpy_array(G))
        # Post_adjacency_matrix(path, matrix)

    # operation_contraction_edge('animation/graf-first', 0, 2)
