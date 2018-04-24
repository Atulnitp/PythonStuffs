
# class Graph to store edges of a G(v,E) in the form of adjacency list  in Python
class Graph(object):
    """docstring for Graph."""

    def __init__(self, V, E):
        super(Graph, self).__init__()
        self.V = V
        self.adjacencyList = [[] for _ in range(self.V)]
        for edge in E:
            self.addEdge(edge[0], edge[1])

    def addEdge(self, u, w):
        self.adjacencyList[u - 1].append(w)
        self.adjacencyList[w - 1].append(u)

    def display(self):
        for i, item in enumerate(self.adjacencyList):
            print("Adjacency list for node ", i+1, ": ", *self.adjacencyList[i])
# input format enter number of vertex V and no of edges E in first line space separated format. following E line
# should be a the vertices with space separated
v , e = input().split()
v , e = int(v), int(e)
edges = []
for _ in range(e):
    edge_t = [int(t) for t in input().split()]
    edges.append(edge_t)
graphObject = Graph(v, edges)
graphObject.display()