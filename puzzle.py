import heapq as hq

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
    # print(easy)
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
    print(puzzle)
    print('\n')

def select_and_init_algorithm(puzzle):
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for Misplaced Tile Heuristic, " +
    "or (3) for Manhattan Distance Heuristic.\n")
    # print(algorithm + '\n')
    search(puzzle, algorithm)

class TreeNode:
    def __init__(self, state=None):
        self.state = state
        self.left = None
        self.right = None
    
    def equal(self,puzzle):
        for i in range(0,3):
            if puzzle[i] != self.state[i]:
                return False
        return True

def search(puzzle,heuristic):
    starting_node = TreeNode(puzzle)
    working_queue = []
    hq.heappush(working_queue,starting_node)
    num_nodes_expanded = 0
    max_queue_size = 0

    stack_to_print = []

    while len(working_queue ) > 0:
        max_queue_size = max(len(working_queue),max_queue_size)
        node_from_queue = hq.heappop(working_queue)
        if node_from_queue.equal(goal_state):
            while len(stack_to_print) > 0:
                print_puzzle(stack_to_print.pop())
                print("Number of nodes expanded: ",num_nodes_expanded)
                print("Max queue size: ",max_queue_size)
                return node_from_queue
        stack_to_print.append(node_from_queue.state)

if __name__ == '__main__':
    main()
