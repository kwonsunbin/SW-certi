from collections import deque

class graph():
    def __init__(self):
        self.graph = {}

    def connect(self, connection):
        a, b = connection 
        if a not in self.graph.keys():
            self.graph[a] = [b]
        else: 
            self.graph[a].append(b)

    def print_graph_info(self):
        print(self.graph)

    def return_graph(self):
        return self.graph

def bfs(graph):
    que = deque()
    res = []
    
    graph = graph.return_graph()
    visited = [0] * len(graph)
    que.extend(graph[0])
    visited[0] = 1
    res.append(0)

    while que :
        i = que.popleft()
        if not visited[i] :
            que.extend(graph[i])
            visited[i] = 1
            res.append(i)

    print(res)

def dfs(graph):
    stack = deque()
    res = []
    
    graph = graph.return_graph()
    visited = [0] * len(graph)
    stack.extend(graph[0][::-1])
    visited[0] = 1
    res.append(0)

    while stack :
        i = stack.pop()
        if not visited[i] :
            stack.extend(graph[i][::-1])
            visited[i] = 1
            res.append(i)

    print(res)

def dfs_recursive(graph):
    res = []
    graph = graph.return_graph()
    visited = [0] * len(graph)
    

    def dfs(idx):
        for i in graph[idx]:
            if not visited[i] :
                visited[i] = 1
                res.append(i)
                dfs(i)

    visited[0] = 1
    res.append(0)
    dfs(0)

    print(res)

if __name__ == "__main__":
    edges = [(0,1),(0,2),(0,3),(1,0),(1,2),(1,3),(2,0),(2,1),(2,3),(2,4),(3,0),(3,1),(3,2),(3,6),(4,2),(4,5),(5,4),(6,3)]
    graph = graph()
    for edge in edges:
        graph.connect(edge)

    graph.print_graph_info()
    bfs(graph)
    dfs(graph)
    dfs_recursive(graph)


