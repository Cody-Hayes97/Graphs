"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            return None

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            curr = q.dequeue()
            if curr not in visited:
                visited.add(curr)
                neighbors = self.get_neighbors(curr)
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        while stack.size() > 0:
            curr = stack.pop()

            if curr not in visited:
                visited.add(curr)
                neighbors = self.get_neighbors(curr)
                for neighbor in neighbors:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        if visited is None:
            visited = set()
        print(starting_vertex)

        neighbors = self.get_neighbors(starting_vertex)
        visited.add(starting_vertex)

        for vertex in neighbors:
            if vertex not in visited:
                self.dft_recursive(vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()
        visited = set()
        queue.enqueue({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })
        while queue.size() > 0:
            curr = queue.dequeue()
            curr_path = curr['path']
            current_vertex = curr['current_vertex']

            if current_vertex not in visited:
                if current_vertex == destination_vertex:
                    return curr_path

                visited.add(current_vertex)
                for vertex in self.get_neighbors(current_vertex):
                    new_path = list(curr_path)
                    new_path.append(vertex)
                    queue.enqueue({
                        'current_vertex': vertex,
                        'path': new_path
                    })

    def dfs(self, starting_vertex, destination_vertex):
        stack = Stack()
        visited = set()
        stack.push({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })
        while stack.size() > 0:
            curr = stack.pop()
            curr_path = curr['path']
            current_vertex = curr['current_vertex']

            if current_vertex not in visited:
                if current_vertex == destination_vertex:
                    return curr_path

                visited.add(current_vertex)
                for vertex in self.get_neighbors(current_vertex):
                    new_path = list(curr_path)
                    new_path.append(vertex)
                    stack.push({
                        'current_vertex': vertex,
                        'path': new_path
                    })

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('1', '0')
# graph.add_edge('0', '3')
# graph.add_edge('3', '0')
# print(graph.vertices)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

#     '''
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
    # print(graph.vertices)

#     '''
#     Valid BFT paths:
#         1, 2, 3, 4, 5, 6, 7
#         1, 2, 3, 4, 5, 7, 6
#         1, 2, 3, 4, 6, 7, 5
#         1, 2, 3, 4, 6, 5, 7
#         1, 2, 3, 4, 7, 6, 5
#         1, 2, 3, 4, 7, 5, 6
#         1, 2, 4, 3, 5, 6, 7
#         1, 2, 4, 3, 5, 7, 6
#         1, 2, 4, 3, 6, 7, 5
#         1, 2, 4, 3, 6, 5, 7
#         1, 2, 4, 3, 7, 6, 5
#         1, 2, 4, 3, 7, 5, 6
#     '''
    # graph.bft(1)

#     '''
#     Valid DFT paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
    # graph.dft(1)
    # graph.dft_recursive(1)

#     '''
#     Valid BFS path:
#         [1, 2, 4, 6]
#     '''
    # print(graph.bfs(1, 6))

#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
    print(graph.dfs(1, 6))
#     print(graph.dfs_recursive(1, 6))
