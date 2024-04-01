from collections import deque
from sys import setrecursionlimit

with open("input10.txt") as f:
    ls = f.read().strip().split("\n")

q = { 10: open("input10.txt").read().strip() }
"""
frontier = {
    "|": [1,-1],
    "-": [1j,-1j],
    "J": [-1, -1j],
    "F": [1, 1j],
    "7": [1, -1j],
    "L": [-1, 1j],
    "S": [1,-1j]
}
board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}
print(board)
S = next(z for z, x in board.items() if x == "S")
explored = {S}
next_elem = deque([(S,0)])
while next_elem:
    curr_elem, dist  = next_elem.popleft()
    for next_dir in frontier[board[curr_elem]]:
        new_dir = curr_elem+next_dir
        if new_dir not in explored:
            next_elem.append((new_dir, dist+1))
            explored.add(new_dir)

print(dist)
"""
setrecursionlimit(30000)

grid = [[x for x in row] for row in q[10].strip().split('\n')]
pipe_map = {'|': [(0, -1), (0, 1)], '-': [(1, 0), (-1, 0)], 
            'L': [(0, -1), (1, 0)], 'J': [(0, -1), (-1, 0)], 
            '7': [(0, 1), (-1, 0)], 'F': [(0, 1), (1, 0)], 
            '.': [], 'S': [(0, -1), (0, 1), (1, 0), (-1, 0)]}

def find_valid_moves(grid, pos, pipe_map, prev_dir=None):
    char = grid[pos[1]][pos[0]]
    valid_directions = pipe_map[char]
    valid_moves = []
    for d in valid_directions:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        new_char = grid[new_pos[1]][new_pos[0]]
        if 0 <= new_pos[0] < len(grid[0]) and 0 <= new_pos[1] < len(grid):
            if d == (0, -1) and (0, 1) in pipe_map[new_char] and prev_dir != (0, 1):
                valid_moves.append(new_pos)
            if d == (0, 1) and (0, -1) in pipe_map[new_char] and prev_dir != (0, -1):
                valid_moves.append(new_pos)
            if d == (1, 0) and (-1, 0) in pipe_map[new_char] and prev_dir != (-1, 0):
                valid_moves.append(new_pos)
            if d == (-1, 0) and (1, 0) in pipe_map[new_char] and prev_dir != (1, 0):
                valid_moves.append(new_pos)
    return valid_moves

def find_start_char(grid, pos, pipe_map):
    valid_moves = find_valid_moves(grid, pos, pipe_map)
    valid_directions = [(x[0]-pos[0], x[1]-pos[1]) for x in valid_moves]
    for k, v in pipe_map.items():
        if v == valid_directions:
            return k

def solve(grid, pos, pipe_map, visited, prev_dir=None):
    move = find_valid_moves(grid, pos, pipe_map, prev_dir)[0]
    if move == start_pos and len(visited) > 0:
        return visited
    visited.add(move)
    return solve(grid, move, pipe_map, visited, (move[0]-pos[0], move[1]-pos[1]))

start_pos = [(x, y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == 'S'][0]
grid[start_pos[1]][start_pos[0]] = find_start_char(grid, start_pos, pipe_map)
visited = solve(grid, start_pos, pipe_map, { start_pos })

print(grid)
print(visited)

contained = set()
for i in range(len(grid)):
    within = False
    for j in range(len(grid[0])-1):
        print(j,i)
        if (j, i) in visited:
            print(grid[i][j])
            if grid[i][j] in ['|', 'L', 'J']:
                print("CHANGING WITHIN")
                within = not within
        elif within:
            print("ADDING")
            contained.add((j, i))

print(len(visited)//2)    
print(contained)  
print(len(contained))
