import heapq as hq
import copy

# globals
# default puzzles
trivial = [['A','N','G'],
           ['E','L','I'],
           ['C','A','.']]

very_easy = [['A','N','G'],
             ['E','L','I'],
             ['C','A','.']]

easy = [['A','N','G'],
        ['E','L','I'],
        ['C','A','.']]

doable = [['A','N','G'],
          ['E','L','I'],
          ['C','A','.']]

oh_boy = [['A','N','G'],
          ['E','L','I'],
          ['C','A','.']]

impossible = [['A','N','G'],
              ['E','L','I'],
              ['C','A','.']]

# goal state
goal_state = [['A','N','G'],
              ['E','L','I'],
              ['C','A','.']]

def main():
    puzzle_mode = input("Welcome to Vivek's ANGELICA-puzzle solver. Type '1' to use default puzzle or '2' to create your own.\n")
    if puzzle_mode == "1":
        select_and_init_algorithm(init_default_puzzle_mode())
    if puzzle_mode == "2":
        print("Enter your own puzzle, using '.' to represent the blank. " +
        "Please only enter valid puzzles. Enter the puzzle delimiting the characters with spaces. RET only when finished.\n")
    
        row_one = input("Enter the first row: ")
        row_two = input("Enter the second row: ")
        row_three = input("Enter the third row: ")

        row_one = row_one.split()
        row_two = row_two.split()
        row_three = row_three.split()

        user_puzzle = [row_one, row_two, row_three]
        select_and_init_algorithm(user_puzzle)

    return

def init_default_puzzle_mode():
    selected_difficulty = input("You wish to use a default puzzle. Please enter a desired difficulty on a scale from 0 to 5.\n")
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

class TreeNode:
    def __init__(self, state=None, g=0, h=0, blank_row=None, blank_col=None):
        self.state = state
        self.blank_row = blank_row
        self.blank_col = blank_col
        self.g = g
        self.h = h
    
    def equal(self,puzzle):
        for i in range(0,3):
            if puzzle[i] != self.state[i]:
                return False
        return True

    def __lt__(self,other):
        return (self.h + self.g) < (other.h + other.g)

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

def expand(node):
    nodes = []
    if node.blank_row > 0:
        # move blank up
        new_node = TreeNode(move(copy.deepcopy(node.state),node.blank_row,node.blank_col,"up"),node.g+1,0,node.blank_row-1,node.blank_col)
        nodes.append(new_node)
        # print("up")
    if node.blank_col > 0:
        # move blank left
        new_node = TreeNode(move(copy.deepcopy(node.state),node.blank_row,node.blank_col,"left"),node.g+1,0,node.blank_row,node.blank_col-1)
        nodes.append(new_node)
        # print("left")
    if node.blank_col < 2:
        # move blank right
        new_node = TreeNode(move(copy.deepcopy(node.state),node.blank_row,node.blank_col,"right"),node.g+1,0,node.blank_row,node.blank_col+1)
        nodes.append(new_node)
        # print("right")
    if node.blank_row < 2:
        # move blank down
        new_node = TreeNode(move(copy.deepcopy(node.state),node.blank_row,node.blank_col,"down"),node.g+1,0,node.blank_row+1,node.blank_col)
        nodes.append(new_node)
        # print("down")

    return nodes

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

    while len(working_queue ) > 0:
        max_queue_size = max(len(working_queue),max_queue_size)
        node_from_queue = hq.heappop(working_queue)
        print("The best state to expand with a g(n) = " + str(node_from_queue.g) + " and h(n) = " + str(node_from_queue.h) + " is...\n")
        print_puzzle(node_from_queue.state)
        if node_from_queue.equal(goal_state): # success
            print("Number of nodes expanded: ",num_nodes_expanded)
            print("Max queue size: ",max_queue_size)
            return True
        # expand node by applying operators
        nodes = expand(node_from_queue)
        for node in nodes:
            hq.heappush(working_queue,node)
        num_nodes_expanded += 1
    
    return False # search failed

if __name__ == '__main__':
    main()
