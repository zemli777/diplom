import graph

gr = graph.Graph("Path")

print(gr.path, gr.some_field)

gr.update_path()

print(gr.path, gr.some_field)