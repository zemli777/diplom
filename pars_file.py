from base import all_db


def Get_adjacency_matrix(filename):
    # cчитывание графа из файла/ обработка матрицы смежности
    adj_matrix = list()
    graphfile = open(filename, 'r')
    for l in graphfile:
        l = l.rstrip()[1:-1].split()
        for i in range(len(l)):
            l[i] = int(l[i])
        adj_matrix.append(l)
    graphfile.close()
    return adj_matrix


def Post_adjacency_matrix(filename, data):
    # запись графа в файл (в виде матрицы смежности)
    graphfile = open(filename, 'w')
    for index1 in data:
        graphfile.write('[')
        for index2 in index1:
            graphfile.write(' ' + str(index2))
        graphfile.write(']\n')
    graphfile.close()
    graphfile = open(filename, 'r')
    st_buf = ''
    for st in graphfile:
        st_buf += st.replace(' ', '', 1)
    graphfile.close()
    graphfile = open(filename, 'w')
    graphfile.write(st_buf)
    graphfile.close()
    return 0


def matrix_nx(matrix):
    matrix = matrix.tolist()
    matrix_buf = []
    for item in matrix:
        buf = []
        for item2 in item:
            buf.append(int(item2))
        matrix_buf.append(buf)
    return matrix_buf


def db_pars():
    print(all_db())
