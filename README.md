# Game-of-Life

## Introduction

Implementation of John Conway's Game of Life. A grid-based generational python flask solution.

### Rules

There are 3 condensed rules that the Game of Life.

1. Any live cell with <2 or >3 live neighbours dies in the next generation.

2. Any dead cell with 3 live neighbours becomes a live cell in the next generation.

3. All other cells die/stay dead in the next generation.

## Thoughts

* 2 2d arrays (or subsitutes) represent the grid current state and a temp future state

* Instantiate grid randomly (at first) with either 0 or 1

* Display grid using black and white for cell live state

* Loop through grid to find 8 adjacent neighbours for each cell

* Count live cells in grid total (end state check)

* Grid edges don't loop
