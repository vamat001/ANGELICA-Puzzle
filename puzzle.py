

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

if __name__ == '__main__':
    main()
