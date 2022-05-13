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
    if selected_difficulty == 0:
        print("Difficulty of 'Trivial' selected.")
        return trivial
    if selected_difficulty == 1:
        print("Difficulty of 'Very Easy' selected.")
        return very_easy
    if selected_difficulty == 2:
        print("Difficulty of 'Easy' selected")
        return easy
    if selected_difficulty == 3:
        print("Difficulty of 'Doable' selected")
        return doable
    if selected_difficulty == 4:
        print("Difficulty of 'Oh Boy' selected")
        return oh_boy
    if selected_difficulty == 5:
        print("Difficulty of 'Impossible' selected")
        return impossible

def print_puzzle(puzzle):
    for i in range(0,3):
        print(puzzle[i])
    print('\n')

if __name__ == '__main__':
    main()
