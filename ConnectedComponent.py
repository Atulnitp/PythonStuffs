
# class Graph to store edges of a G(v,E) and finding all connected component in the given Graph  in Python

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

    def addEdge(self, u, w):
        self.adjacencyList[u - 1].append(w)
        self.adjacencyList[w - 1].append(u)

    def display(self):
        for i, item in enumerate(self.adjacencyList):
            print("Adjacency list for node ", i+1, ": ", *self.adjacencyList[i])
        print("Number of Connected Component in Graph : ", len(self.connComp))
        for i, comp in enumerate(self.connComp):
            print("Connected component number ", i+1, ":", comp)

    def ConnectedComponent(self):
        self.visited = [False for _ in range(self.V)]
        self.connComp = []
        for j in range(self.V):
            if self.visited[j] == False:
                temp = self.BreathFirstSearch(j + 1)  # j index is node number j+1
                self.connComp.append(temp)
        return self.connComp

    def BreathFirstSearch(self, start):
        queue = deque()
        connectedComponent = set()
        # mark start as visited
        self.visited[start - 1] = True
        queue.append(start)
        while len(queue):
            node = queue.popleft()
            connectedComponent.add(node)
            for x in self.adjacencyList[node - 1]:
                if not self.visited[x - 1]:
                    self.visited[x - 1] = True
                    queue.append(x)
        return connectedComponent

# input format enter number of vertex V and no of edges E in first line space separated format. following E line
# should be a the vertices with space separated
v , e = input().split()
v , e = int(v), int(e)
edges = []
for _ in range(e):
    edge_t = [int(t) for t in input().split()]
    edges.append(edge_t)
graphObject = Graph(v, edges)
graphObject.ConnectedComponent()
graphObject.display()