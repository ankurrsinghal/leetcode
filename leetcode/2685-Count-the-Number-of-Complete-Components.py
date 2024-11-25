from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Graph initialization
        graph = defaultdict(list)
        
        # Build the graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Visited array to track which component each node belongs to
        visited = [-1] * n
        
        # Helper function to perform DFS and collect nodes/edges for a component
        def dfs(node, component_id):
            stack = [node]
            nodes = 0
            edge_count = 0
            visited[node] = component_id
            
            while stack:
                u = stack.pop()
                nodes += 1
                for v in graph[u]:
                    edge_count += 1
                    if visited[v] == -1:
                        visited[v] = component_id
                        stack.append(v)
            
            # Each edge is counted twice in an undirected graph (u-v and v-u)
            edge_count //= 2
            
            return nodes, edge_count
        
        # Variable to count complete components
        complete_component_count = 0
        current_component = 0
        
        # Traverse all nodes to find all components
        for node in range(n):
            if visited[node] == -1:
                # Perform DFS to find all nodes and edges in this component
                nodes_in_component, edges_in_component = dfs(node, current_component)
                
                # A component is complete if it has exactly `nodes_in_component * (nodes_in_component - 1) // 2` edges
                if edges_in_component == nodes_in_component * (nodes_in_component - 1) // 2:
                    complete_component_count += 1
                
                # Move to the next component ID
                current_component += 1
        
        return complete_component_count
