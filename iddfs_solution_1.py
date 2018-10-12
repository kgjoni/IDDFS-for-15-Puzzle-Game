import sys
import psutil
import random
import itertools
import time
import math
import os
import copy

# List storing all moves
M = []

# Count number of nodes expanded
node_expanded = 0


def run_depth_first_search(path, limit, target, next_step):
    """ Implement depth first search """

    # Checked all nodes, no solution
    if limit == 0:
        return

    # Target = User Input, solution found
    if path[-1] == target:
        # Print all moves as a string
        print("Moves:", ",".join(str(x) for x in M))
        # Print total number of nodes checked
        print("Node expanded:", len(M))
        return path

    # For-loop
    for x in next_step(path[-1]):

        # Index not in path
        if x not in path:
            # Run depth first search
            solution = run_depth_first_search(path + [x], (limit - 1), target, next_step)

            # Solution found
            if solution:
                return solution     # return solution


def run_iterative_deepening_search(new_list, target, next_step):
    """ Implement iterative deepening depth first search """
    
    # For-loop
    for limit in itertools.count():

        # Run depth first search
        path = run_depth_first_search([new_list], limit, target, next_step)
        
        # Path found
        if path:
            return path     # return path


def board_size(R, C):
    """ 15 sliding puzzle (works for other board sizes!) """

    def next_step(puzzle):
        """ List all moves executed """

        step = []
        m, n = next((m2,n2)

        # For-loop over puzzle, keeping a counter
        for m2, index1 in enumerate(puzzle)

            # For-loop over single list, keeping a counter
            for n2, index2 in enumerate(index1) if index2 == 0)

        def shift(e1, e2):
            """ Switch position of tiles """

            # Make a copy of the puzzle
            next_puzzle = copy.deepcopy(puzzle)

            # Switch position of tiles
            next_puzzle[m][n], next_puzzle[e1][e2] = next_puzzle[e1][e2], next_puzzle[m][n]
            return next_puzzle
            # end shift()

        # Count of nodes expanded
        node_expanded = 0

        # Make a move Down
        if m < (R - 1):
            # Update node expanded counter
            node_expanded = node_expanded + 1
            # Append 'R' to moves
            M.append("D")
            step.append(shift((m + 1), n))

        # Make a move Left
        if n > 0:
            # Update node expanded counter
            node_expanded = node_expanded + 1
            # Append 'R' to moves
            M.append("L")
            step.append(shift(m, (n - 1)))
        
        # Make a move Up
        if m > 0:
            # Update node expanded counter
            node_expanded = node_expanded + 1
            # Append 'R' to moves
            M.append("U")
            step.append(shift((m - 1), n))

        # Make a move Right
        if n < (C - 1):
            # Update node expanded counter
            node_expanded = node_expanded + 1
            # Append 'R' to moves
            M.append("R")
            step.append(shift(m, (n + 1)))
                    
        return step
        # end next_step()

    return next_step
    # end board_size()


def main():

    # 4x4 board
    # rows, columns = 4

    while True:

        user_input = input("Enter numbers:\n")
        
        # Error check: input too short (number is missing)
        if len(user_input) < 37:
            print("Input incorrect. Try again...")
            continue

        # Get input from user and convert it into a list 
        user_input = user_input.replace(" ", ",")
        new_user_input = [str(k) for k in user_input.split(',')]
        new_user_input = list(map(int, new_user_input))
        new_list = []

        # Convert input into a list of lists
        for i in range(0, len(new_user_input), 4):
            new_list.append(new_user_input[i:i+4])
        
        # Final target puzzle
        target = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    
        # Start calculating memory usage
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss / 1024.0
    
        node_expanded = 0

        # Start time
        starting_time = time.time()

        print("\nRESULTS\n")

        # Run IDDFS on input
        run_iterative_deepening_search(new_list, target, board_size(4, 4))
        
        # End time
        ending_time = time.time()
        
        #Calculate total time (rounded in milliseconds, ms)
        total_time = (ending_time - starting_time)
        total_time = int(round(total_time * 1000))

        print("Time Taken:", total_time, "ms (milliseconds)")

        # Calculate and print memory usage
        final_memory = process.memory_info().rss / 1024.0
        print("Memory Used:", str(final_memory-initial_memory) + " KB")

        break

if __name__=="__main__":main()

