

goal = "123456780"

moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}


def dfs(start):
    stack = [(start, 0)]
    visited = set()

    while stack:

        state, count = stack.pop()

        if state == goal:
            return count

        if state in visited:
            continue

        visited.add(state)

        zero = state.index("0")

        for pos in moves[zero]:

            s = list(state)
            s[zero], s[pos] = s[pos], s[zero]

            new_state = "".join(s)

            if new_state not in visited:
                stack.append((new_state, count + 1))

    return -1


def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3].replace("0", " "))


# New Initial State
start = "123456708"

result = dfs(start)

print("INITIAL STATE:")
display(start)

print("\nGOAL STATE:")
display(goal)

if result != -1:
    print("\nRESULT: SOLUTION FOUND")
    print("NUMBER OF MOVES:", result)
else:
    print("\nRESULT: SOLUTION NOT FOUND")
    print("NUMBER OF MOVES: 0")
