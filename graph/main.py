import graph
from graph import Vertex

М = Vertex('М', [])
К = Vertex('К', [М])
Л = Vertex('Л', [М])
И = Vertex('И', [К, Л])
Ж = Vertex('Ж', [И])
Е = Vertex('Е', [И, Ж])
З = Vertex('З', [И, Ж])
В = Vertex('В', [Е, Ж, З])
Б = Vertex('Б', [В, Е])
Г = Vertex('Г', [В, З])
Д = Vertex('Д', [Г, З])
А = Vertex('А', [Б, В, Г, Д])

paths = graph.search_path(А, М)
with_ = graph.filter_with_branch(paths, Ж)
out = graph.filter_without_branch(with_, К)
print(*out, sep='\n')
print(len(out))