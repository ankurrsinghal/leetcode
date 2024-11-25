class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        rows, cols = len(board), len(board[0])
        # Convert the board to a tuple of tuples for efficient hashing
        start = tuple(sum(board, []))
        target = (1, 2, 3, 4, 5, 0)
        
        # Directions for moving the zero (up, down, left, right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Function to check if the current board state is the solution
        def win(node):
            return node == target
        
        # Function to generate all possible moves from the current board state
        def get_neighbors(node):
            # Find the position of '0'
            zero_pos = node.index(0)
            row, col = divmod(zero_pos, cols)
            neighbors = []
            
            for dy, dx in directions:
                r, c = row + dy, col + dx
                if 0 <= r < rows and 0 <= c < cols:
                    new_pos = r * cols + c
                    # Create a new board state by swapping positions of '0' and the new element
                    new_node = list(node)
                    new_node[zero_pos], new_node[new_pos] = new_node[new_pos], new_node[zero_pos]
                    neighbors.append(tuple(new_node))
            
            return neighbors
        
        # BFS setup
        q = deque([start])
        visited = {start}
        moves = 0
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if win(node):
                    return moves
                for neighbor in get_neighbors(node):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            moves += 1
        
        return -1