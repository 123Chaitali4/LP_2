from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}  # This will store the graph as an adjacency list

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Since the graph is undirected

    def dfs(self, vertex, visited=None):
        if visited is None:
            visited = set()

        # Mark the node as visited and print it
        visited.add(vertex)
        print(vertex, end=" ")

        # Recur for all the adjacent vertices
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()  # To track visited vertices
        queue = deque([start])  # Queue for BFS

        while queue:
            vertex = queue.popleft()  # Dequeue the first element
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=" ")

                # Enqueue all the adjacent vertices
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

# Function to get user input for graph edges and perform DFS or BFS
def main():
    g = Graph()

    # Get number of edges
    num_edges = int(input("Enter number of edges: "))

    # Take user input for each edge
    for _ in range(num_edges):
        u, v = map(int, input("Enter edge (u v): ").split())
        g.add_edge(u, v)

    while True:
        # Ask user for which search to perform
        search_type = input("Which search would you like to perform? (DFS/BFS): ").strip().lower()

        # Get starting vertex
        start_vertex = int(input("Enter the starting vertex: "))

        # Perform the chosen search
        if search_type == "dfs":
            print("\nDFS traversal:")
            g.dfs(start_vertex)
        elif search_type == "bfs":
            print("\nBFS traversal:")
            g.bfs(start_vertex)
        else:
            print("Invalid search type! Please choose either 'DFS' or 'BFS'.")
        
        # Ask if the user wants to perform another search
        another_search = input("\nWould you like to perform another search? (yes/no): ").strip().lower()
        if another_search != 'yes':
            break

# Run the program
if __name__ == "__main__":
    main()






# OUTPUT:-
# PS C:\Users\Asus\OneDrive\Desktop\LP2> python 1st.py
# Enter number of edges: 5  
# Enter edge (u v): 1 2
# Enter edge (u v): 1 3
# Enter edge (u v): 2 4
# Enter edge (u v): 2 5
# Enter edge (u v): 3 6
# Which search would you like to perform? (DFS/BFS): dfs
# Enter the starting vertex: 1

# DFS traversal:
# 1 2 4 5 3 6
# Would you like to perform another search? (yes/no): yes
# Which search would you like to perform? (DFS/BFS): bfs
# Enter the starting vertex: 1

# BFS traversal:
# 1 2 3 4 5 6
# Would you like to perform another search? (yes/no): no
# PS C:\Users\Asus\OneDrive\Desktop\LP2> 