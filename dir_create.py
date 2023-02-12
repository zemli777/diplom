import os
import hmac, hashlib
import random
import sqlite3


def dir_graf(operation):
    dir = hmac.new(bytearray('signature', 'utf-8'), bytearray(str(random.random()), 'utf-8'),
                   hashlib.sha256).hexdigest()
    os.mkdir(f'graph_view/{dir}')
    graphfile_first = open(f'graph_view/{dir}/graph-first-{operation}', 'w')
    graphfile_second = open(f'graph_view/{dir}/graph-second-{operation}', 'w')
    graphfile_result = open(f'graph_view/{dir}/graph-result-{operation}', 'w')

    graphfile_first_name = graphfile_first.name
    graphfile_second_name = graphfile_second.name
    graphfile_result_name = graphfile_result.name

    graphfile_first.close()
    graphfile_second.close()
    graphfile_result.close()

    return [f'graph_view/{dir}', graphfile_first_name, graphfile_second_name, graphfile_result_name]

# print(dir_graf('sum'))
