import heapq

GOAL = (
    (1, 2, 3),
    (8, 0, 4),
    (7, 6, 5)
)

GOAL_POS = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    8: (1, 0), 0: (1, 1), 4: (1, 2),
    7: (2, 0), 6: (2, 1), 5: (2, 2)
}

def h_misplaced(state):
    count = 0
    for r in range(3):
        for c in range(3):
            if state[r][c] != 0 and state[r][c] != GOAL[r][c]:
                count += 1
    return count

def h_manhattan(state):
    dist = 0
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0:
                gr, gc = GOAL_POS[val]
                dist += abs(r - gr) + abs(c - gc)
    return dist

def get_neighbors(state):
    neighbors = []
    zero_r, zero_c = 0, 0
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                zero_r, zero_c = r, c
                break

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = zero_r + dr, zero_c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            board = [list(row) for row in state]
            board[zero_r][zero_c], board[nr][nc] = board[nr][nc], board[zero_r][zero_c]
            neighbors.append(tuple(tuple(row) for row in board))
            
    return neighbors

def a_star(initial_state, heuristic_func):
    h_start = heuristic_func(initial_state)
    open_set = [(h_start, 0, initial_state, [initial_state])]
    visited = {initial_state: 0}

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == GOAL:
            return path, g

        for neighbor in get_neighbors(current):
            new_g = g + 1
            if neighbor not in visited or new_g < visited[neighbor]:
                visited[neighbor] = new_g
                new_f = new_g + heuristic_func(neighbor)
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None, -1

def print_solution(path, moves):
    if path is None:
        print("Solution Not Found")
        return
    print("Solution Found")
    print("Number of moves:", moves)
    print()
    for step_num, state in enumerate(path):
        print("Step", step_num)
        for row in state:
            print(" ".join("_" if x == 0 else str(x) for x in row))
        print()

initial = (
    (2, 8, 3),
    (1, 6, 4),
    (7, 0, 5)
)

path1, moves1 = a_star(initial, h_misplaced)
print_solution(path1, moves1)

path2, moves2 = a_star(initial, h_manhattan)
print_solution(path2, moves2)
