class Game:
    def __init__(self):
        # None means empty cell
        self.board = [[None for _ in range(3)] for _ in range(3)]

    def display_board(self, numbers=None):
        show_numbers_x = numbers in ('x', 'both')
        show_numbers_y = numbers in ('y', 'both')

        for row_count, row in enumerate(self.board):
            if row_count != 0:
                print("-" * 11)

            for col_count, col in enumerate(row):
                # Show row numbers
                if col_count == 0 and show_numbers_x:
                    print(f"{row_count + 1} ", end="")
                elif col_count == 0:
                    print("  ", end="")

                # Show the cell content
                col = ' ' if col is None else col
                print(col, end="")

                # Column separator
                if col_count != 2:
                    print(" | ", end="")
            print()  # End of row

        # Show column numbers at bottom
        if show_numbers_y:
            print("  1   2   3")
        print()  # Final newline

    def place_piece(self, piece, x_pos, y_pos):
        self.board[y_pos][x_pos] = piece  # row = y, col = x

# Utility to check if all elements in a list are equal
all_equal = lambda lst: lst.count(lst[0]) == len(lst) and lst[0] is not None

def check_win(game):
    board = game.board
    # Check rows
    for row in board:
        if all_equal(row):
            game.display_board()
            winner_message(row[0])

    # Check columns
    for i in range(3):
        col = [board[0][i], board[1][i], board[2][i]]
        if all_equal(col):
            game.display_board()
            winner_message(col[0])

    # Check diagonals
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]
    for diag in [diag1, diag2]:
        if all_equal(diag):
            game.display_board()
            winner_message(diag[0])

def winner_message(piece):
    print(f"{piece.upper()} wins!")
    from sys import exit
    exit()

def play(game, piece):
    print(f"{piece.upper()}'s turn.")

    while True:
        game.display_board(numbers='y')
        try:
            y_pos = int(input("Choose Y position (row 1-3): ")) - 1
            x_pos = int(input("Choose X position (column 1-3): ")) - 1
        except ValueError:
            print("Please enter valid numbers 1-3.")
            continue

        if not (0 <= x_pos <= 2 and 0 <= y_pos <= 2):
            print("Positions must be between 1 and 3.")
            continue

        if game.board[y_pos][x_pos] is None:
            game.place_piece(piece, x_pos, y_pos)
            break
        else:
            print("That cell is already occupied, try again.")

# Start the game
game = Game()

while True:
    play(game, 'x')
    check_win(game)
    play(game, 'o')
    check_win(game)
