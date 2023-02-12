import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

from pars_file import Get_adjacency_matrix
from pars_file import Post_adjacency_matrix
from pars_file import matrix_nx
from dir_create import dir_graf
from base import all_db, add_to_db, dell_from_db_from_name, dell_from_db_drom_path, find_db_from_path, \
    find_db_from_name, edit_db_name


path = '/home/schemotechnik/PycharmProjects/diplom/graph_view/32a9efae6459611c787a6b9945e9ac54fb8b1a53752be45740d3741a88a83689/graph-first-create_new_graph'
adj_max = Get_adjacency_matrix(path)

G = nx.DiGraph(np.matrix(adj_max))
nx.draw(G, pos=nx.planar_layout(G), with_labels=True, node_size=500, arrows=True)
plt.show()
#plt.savefig(path)
plt.close()