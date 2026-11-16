import random
import math

def display(board):
    for i in range(len(board)):
        print(" ".join("Q" if board[i] == j else "." for j in range(len(board))))
    print()

def cost(board):
    count = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                count += 1
    return count

def simulated_annealing(n):
    while True:
        board = [random.randrange(n) for _ in range(n)]
        print("Initial Board:")
        display(board)
        print("Initial Cost:", cost(board))

        temp = 100

        while temp > 0.1:
            old = cost(board)

            if old == 0:
                print("Final Board:")
                display(board)
                print("Final Cost:", old)
                print("Solution Found!")
                return

            new = board.copy()
            row = random.randrange(n)
            new[row] = random.randrange(n)

            new_cost = cost(new)

            if new_cost < old or random.random() < math.exp((old - new_cost) / temp):
                board = new

            temp *= 0.99

simulated_annealing(8)