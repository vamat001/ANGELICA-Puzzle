import heapq as hq
import copy
from datetime import datetime

# globals
# default puzzles
trivial = [['A','N','G'],
           ['E','L','.'],
           ['C','a','I']]

very_easy = [['A','N','G'],
             ['E','L','I'],
             ['.','C','a']]

easy = [['A','N','G'],
        ['L','.','I'],
        ['E','C','a']]

doable = [['A','G','I'],
          ['L','.','N'],
          ['E','C','a']]

oh_boy = [['A','I','C'],
          ['L','.','G'],
          ['E','a','N']]

impossible = [['.','C','N'],
              ['E','I','A'],
              ['G','L','a']]

destruction = [['a','I','C'],
              ['N','L','E'],
              ['G','.','A']]

# goal state
goal_state = [['A','N','G'],
              ['E','L','I'],
              ['C','a','.']]

class TreeNode:
    def __init__(self, state=None, g=0, h=0, blank_row=None, blank_col=None):
        self.state = state
        self.blank_row = blank_row
        self.blank_col = blank_col
        self.g = g
        self.h = h

    # overide built in comparison function for using heapq
    def __lt__(self,other):
        return (self.h + self.g) < (other.h + other.g) # f(n) = g(n) + h(n)

# print a puzzle
def print_puzzle(puzzle):
    for i in range(0,3):
        print("[%s]" % (', '.join(puzzle[i])))
    print('\n')

def select_and_init_algorithm(puzzle):
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for Misplaced Tile Heuristic, " +
    "or (3) for Manhattan Distance Heuristic.\n")
    # print(algorithm + '\n')
    if not(search(puzzle, algorithm)):
        print("\nSearch failed!\n")

# calculate different heuristics
def calc_heuristic(puzzle, heuristic):
    if heuristic == "1": # uniform cost
        return 0
    if heuristic == "2": # misplaced tile
        misplaced_tiles = 0
        for i in range(0,3):
            for j in range(0,3):
                if puzzle[i][j] != goal_state[i][j]:
                    misplaced_tiles += 1
        return misplaced_tiles
    if heuristic == "3": # manhattan distance
        coords = dict()
        # store coordinates of one puzzle in dict for comparison
        for i in range(0,3):
            for j in range(0,3):
                coords[puzzle[i][j]] = (i,j)
        dist = 0
        for i in range(0,3):
            for j in range(0,3):
                coord = coords[goal_state[i][j]]
                # print(puzzle[coord[0]][coord[1]] + " " + goal_state[i][j] + str(coord) + " " + str((i,j)))
                dist += abs(coord[0] - i) + abs(coord[1] - j)

        return dist

def move(puzzle, row, col, direction):
    # print_puzzle(puzzle)
    if direction == "up":
        # move blank up
        puzzle[row-1][col], puzzle[row][col] = puzzle[row][col], puzzle[row-1][col]
    if direction == "down":
        # move blank down
        puzzle[row+1][col], puzzle[row][col] = puzzle[row][col], puzzle[row+1][col]
    if direction == "left":
        # move blank left
        puzzle[row][col-1], puzzle[row][col] = puzzle[row][col], puzzle[row][col-1]
    if direction == "right":
        # move blank right
        puzzle[row][col+1], puzzle[row][col] = puzzle[row][col], puzzle[row][col+1]

    # print_puzzle(puzzle)
    return puzzle

def expand(node, heuristic):
    nodes = []
    if node.blank_row > 0:
        # move blank up
        new_node = TreeNode(move(copy.deepcopy(node.state),node.blank_row,node.blank_col,"up"),node.g+1,0,node.blank_row-1,node.blank_col)
        # apply heuristic
        new_node.h = calc_heuristic(new_node.state, heuristic)
        nodes.append(new_node)
        # print("up")
    if node.blank_col > 0:
        # move blank left
        new_node = TreeNode(move(copy.deepcopy(node.state),node.blank_row,node.blank_col,"left"),node.g+1,0,node.blank_row,node.blank_col-1)
        # apply heuristic
        new_node.h = calc_heuristic(new_node.state, heuristic)
        nodes.append(new_node)
        # print("left")
    if node.blank_col < 2:
        # move blank right
        new_node = TreeNode(move(copy.deepcopy(node.state),node.blank_row,node.blank_col,"right"),node.g+1,0,node.blank_row,node.blank_col+1)
        # apply heuristic
        new_node.h = calc_heuristic(new_node.state, heuristic)
        nodes.append(new_node)
        # print("right")
    if node.blank_row < 2:
        # move blank down
        new_node = TreeNode(move(copy.deepcopy(node.state),node.blank_row,node.blank_col,"down"),node.g+1,0,node.blank_row+1,node.blank_col)
        # apply heuristic
        new_node.h = calc_heuristic(new_node.state, heuristic)
        nodes.append(new_node)
        # print("down")

    return nodes

def to_tuple(puzzle):
    return tuple(map(tuple,puzzle))

def search(puzzle,heuristic):
    starting_node = TreeNode(puzzle)
    for i in range(0,3):
        if "." in puzzle[i]:
            starting_node.blank_row = i
            starting_node.blank_col = puzzle[i].index(".")
    
    # print(str(starting_node.blank_row) + " " + str(starting_node.blank_col) + '\n')

    working_queue = []
    hq.heappush(working_queue,starting_node)
    num_nodes_expanded = 0
    max_queue_size = 0
    repeated_states = dict()
    start = datetime.now()
    while len(working_queue ) > 0:
        max_queue_size = max(len(working_queue),max_queue_size)
        node_from_queue = hq.heappop(working_queue)
        # if we have reached a repeated state then take the state with the lower path cost
        hashable_state = to_tuple(node_from_queue.state)
        if hashable_state in repeated_states:
            if node_from_queue.g + node_from_queue.h > repeated_states[hashable_state]:
                continue
        else:
            repeated_states[hashable_state] = node_from_queue.g + node_from_queue.h
        print("The best state to expand with a g(n) = " + str(node_from_queue.g) + " and h(n) = " + str(node_from_queue.h) + " is...\n")
        print_puzzle(node_from_queue.state)
        if node_from_queue.state == goal_state: # success
            print("Number of nodes expanded: ",num_nodes_expanded)
            print("Max queue size: ",max_queue_size)
            print(datetime.now() - start)
            return True
        # expand node by applying operators
        nodes = expand(node_from_queue, heuristic)
        for node in nodes:
            hq.heappush(working_queue,node)
        num_nodes_expanded += 1
    
    return False # search failed

# default puzzle sub menu
def init_default_puzzle_mode():
    selected_difficulty = input("You wish to use a default puzzle. Please enter a desired difficulty on a scale from 0 to 6.\n")
    # print(selected_difficulty + '\n')
    if selected_difficulty == "0":
        print("Difficulty of 'Trivial' selected.")
        return trivial
    if selected_difficulty == "1":
        print("Difficulty of 'Very Easy' selected.")
        return very_easy
    if selected_difficulty == "2":
        print("Difficulty of 'Easy' selected")
        return easy
    if selected_difficulty == "3":
        print("Difficulty of 'Doable' selected")
        return doable
    if selected_difficulty == "4":
        print("Difficulty of 'Oh Boy' selected")
        return oh_boy
    if selected_difficulty == "5":
        print("Difficulty of 'Impossible' selected")
        return impossible
    if selected_difficulty == "6":
        print("Difficulty of 'Destruction' selected")
        return destruction

# main driver function
def main():
    puzzle_mode = input("Welcome to Vivek's ANGELICA-puzzle solver. Type '1' to use default puzzle or '2' to create your own.\n")
    if puzzle_mode == "1":
        select_and_init_algorithm(init_default_puzzle_mode())
    if puzzle_mode == "2":
        print("Enter your own puzzle, using '.' to represent the blank. " +
        "Please only enter valid puzzles. Enter the puzzle delimiting the characters with spaces.\nUse lower case 'a' to denote the second 'A' in 'ANGELICa'. RET only when finished.\n")
    
        row_one = input("Enter the first row: ")
        row_two = input("Enter the second row: ")
        row_three = input("Enter the third row: ")

        row_one = row_one.split()
        row_two = row_two.split()
        row_three = row_three.split()

        user_puzzle = [row_one, row_two, row_three]
        select_and_init_algorithm(user_puzzle)

    return

if __name__ == '__main__':
    main()
