document.getElementById('generate').addEventListener('click', function() {
    fetch('/generate_maze')
    .then(response => response.json())
    .then(data => {
        const maze = data.maze;
        const path = data.path;
        generateMaze(maze, path);
    });
});

function generateMaze(maze, path) {
    const mazeContainer = document.getElementById('maze-container');
    mazeContainer.innerHTML = '';  // Clear the previous maze

    // Create maze cells
    maze.forEach((row, rIdx) => {
        row.forEach((cell, cIdx) => {
            const div = document.createElement('div');
            div.classList.add('cell');
            if (cell === 1) {
                div.classList.add('wall');
            }
            if (rIdx === 0 && cIdx === 0) {
                div.classList.add('start');
            }
            if (rIdx === maze.length - 1 && cIdx === maze[0].length - 1) {
                div.classList.add('goal');
            }
            mazeContainer.appendChild(div);
        });
    });

    // Highlight the path
    path.forEach((step, idx) => {
        setTimeout(() => {
            const rIdx = step[0];
            const cIdx = step[1];
            const index = rIdx * maze[0].length + cIdx;
            const cell = mazeContainer.children[index];
            cell.classList.add('path');
        }, idx * 100);
    });
}
