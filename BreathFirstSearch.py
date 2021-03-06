# class Graph to store edges of a G(v,E) and perform the Breath first search starting from a start vertex over
#  the Graph(V,E)  in Python

from collections import deque


class Graph(object):
    """docstring for Graph."""

    def __init__(self, V, E):
        super(Graph, self).__init__()
        self.V = V
        self.adjacencyList = [[] for _ in range(self.V)]
        self.connComp = []
        for edge in E:
            self.addEdge(edge[0], edge[1])
        self.visited = [False for _ in range(self.V)]

    def addEdge(self, u, w):
        self.adjacencyList[u - 1].append(w)
        self.adjacencyList[w - 1].append(u)

    def display(self):
        for i, item in enumerate(self.adjacencyList):
            print("Adjacency list for node ", i + 1, ": ", *self.adjacencyList[i])

    def breathFirstSearch(self, start):
        self.visited = [False for _ in range(self.V)]
        queue = deque()
        # mark start as visited
        self.visited[start - 1] = True
        queue.append(start)
        while len(queue):
            node = queue.popleft()
            for x in self.adjacencyList[node - 1]:
                if not self.visited[x - 1]:
                    self.visited[x - 1] = True
                    queue.append(x)



# input format enter number of vertex V and no of edges E in first line space separated format. following E line
# should be a the vertices with space separated
v, e = input().split()
v, e = int(v), int(e)
edges = []
for _ in range(e):
    edge_t = [int(t) for t in input().split()]
    edges.append(edge_t)
graphObject = Graph(v, edges)

start = int(input())
graphObject.breathFirstSearch(start)
graphObject.display()