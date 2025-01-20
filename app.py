from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Constants for the maze dimensions
MAZE_ROWS = 10
MAZE_COLS = 10

# Directions for moving in the grid: (row, col)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS Algorithm to find the shortest path
def bfs(maze, start, goal):
    queue = [start]
    parent_map = {start: None}
    visited = set()
    visited.add(start)

    while queue:
        current = queue.pop(0)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent_map[current]
            return path[::-1]  # Reversed to get path from start to goal
        
        # Explore neighbors
        for dr, dc in DIRECTIONS:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and (nr, nc) not in visited and maze[nr][nc] == 0:
                visited.add((nr, nc))
                parent_map[(nr, nc)] = current
                queue.append((nr, nc))
    return []  # Return an empty path if no path is found

# Generate a random maze with walls and paths
def generate_maze(rows, cols):
    maze = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = maze[rows-1][cols-1] = 0  # Ensure start and goal are open
    return maze

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_maze')
def generate_and_solve():
    maze = generate_maze(MAZE_ROWS, MAZE_COLS)
    start = (0, 0)
    goal = (MAZE_ROWS-1, MAZE_COLS-1)
    path = bfs(maze, start, goal)
    return jsonify(maze=maze, path=path)

if __name__ == '__main__':
    app.run(debug=True)
